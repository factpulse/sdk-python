"""
FactPulse SDK - Thin HTTP wrapper with auto-polling.

Usage:
    client = FactPulseClient("email", "password", "client_uid")

    # Option 1: Explicit path (recommended)
    result = client.post("processing/invoices/submit-complete-async",
        invoiceData={...},
        sourcePdf=base64.b64encode(pdf).decode(),
        destination={"type": "afnor"}
    )
    pdf_bytes = result["content"]  # auto-decoded, auto-polled

    # Option 2: Dynamic endpoint builder
    result = client.processing.invoices.submit_complete_async(
        invoiceData={...},
        sourcePdf=base64.b64encode(pdf).decode(),
        destination={"type": "afnor"}
    )

    # GET request
    structure = client.get("chorus-pro/structures/123")
"""
import base64
import threading
import time
from typing import Any, Optional
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class FactPulseError(Exception):
    def __init__(self, message: str, status_code: int = None, details: list = None):
        super().__init__(message)
        self.status_code = status_code
        self.details = details or []


class FactPulseClient:
    def __init__(
        self,
        email: str,
        password: str,
        client_uid: str,
        api_url: str = "https://factpulse.fr",
        timeout: int = 60,
        polling_timeout: int = 120,
        max_retries: int = 3,
    ):
        self._api_url = api_url.rstrip("/")
        self._email = email
        self._password = password
        self._client_uid = client_uid
        self._timeout = timeout
        self._polling_timeout = polling_timeout

        self._token: Optional[str] = None
        self._token_expires_at: float = 0
        self._token_lock = threading.Lock()

        self._session = requests.Session()
        retry = Retry(
            total=max_retries,
            backoff_factor=0.5,
            status_forcelist=[502, 503, 504],
            allowed_methods=["GET", "POST"],
        )
        self._session.mount("https://", HTTPAdapter(max_retries=retry))
        self._session.mount("http://", HTTPAdapter(max_retries=retry))

    def __getattr__(self, name: str) -> "_Endpoint":
        if name.startswith("_"):
            raise AttributeError(name)
        return _Endpoint(self, name.replace("_", "-"))

    def post(self, path: str, **data) -> Any:
        """POST request to /api/v1/{path}"""
        return self._do_request("POST", path, data, retry_auth=True)

    def get(self, path: str, **params) -> Any:
        """GET request to /api/v1/{path}"""
        return self._do_request("GET", path, params, retry_auth=True)

    def _request(self, method: str, path: str, **kwargs) -> Any:
        return self._do_request(method, path, kwargs, retry_auth=True)

    def _do_request(self, method: str, path: str, kwargs: dict, retry_auth: bool) -> Any:
        self._ensure_auth()
        url = f"{self._api_url}/api/v1/{path}"
        headers = {"Authorization": f"Bearer {self._token}"}

        try:
            if method == "GET":
                response = self._session.get(url, headers=headers, params=kwargs, timeout=self._timeout)
            else:
                response = self._session.post(url, headers=headers, json=kwargs, timeout=self._timeout)
        except requests.RequestException as e:
            raise FactPulseError(f"Network error: {e}") from e

        if response.status_code == 401 and retry_auth:
            self._invalidate_token()
            return self._do_request(method, path, kwargs, retry_auth=False)

        data = self._parse_response(response)

        if isinstance(data, dict) and "taskId" in data:
            data = self._poll(data["taskId"])

        if isinstance(data, dict) and "content_b64" in data:
            data["content"] = base64.b64decode(data.pop("content_b64"))

        return data

    def _parse_response(self, response: requests.Response) -> Any:
        try:
            data = response.json()
        except ValueError:
            if response.ok:
                return {"raw": response.content}
            raise FactPulseError(f"HTTP {response.status_code}: {response.text[:500]}", response.status_code)

        if not response.ok:
            if isinstance(data, dict):
                msg = data.get("detail") or data.get("errorMessage") or data.get("message")
                if isinstance(msg, list):
                    details = msg
                    msg = "; ".join(f"{e.get('loc', ['?'])[-1]}: {e.get('msg', '?')}" for e in msg if isinstance(e, dict))
                    raise FactPulseError(f"Validation error: {msg}", response.status_code, details)
                if msg:
                    raise FactPulseError(str(msg), response.status_code)
            raise FactPulseError(f"HTTP {response.status_code}", response.status_code)

        return data

    def _poll(self, task_id: str) -> dict:
        start = time.monotonic()
        interval = 1.0

        while True:
            elapsed = time.monotonic() - start
            if elapsed >= self._polling_timeout:
                raise FactPulseError(f"Polling timeout after {self._polling_timeout}s for task {task_id}")

            self._ensure_auth()
            try:
                response = self._session.get(
                    f"{self._api_url}/api/v1/processing/tasks/{task_id}/status",
                    headers={"Authorization": f"Bearer {self._token}"},
                    timeout=self._timeout,
                )
            except requests.RequestException as e:
                raise FactPulseError(f"Network error while polling: {e}") from e

            if response.status_code == 401:
                self._invalidate_token()
                continue

            data = self._parse_response(response)
            status = data.get("status")

            if status == "SUCCESS":
                return data.get("result") or {}
            if status == "FAILURE":
                result = data.get("result") or {}
                raise FactPulseError(result.get("errorMessage") or "Task failed", details=result.get("details"))

            time.sleep(min(interval, max(0, self._polling_timeout - elapsed)))
            interval = min(interval * 1.5, 10)

    def _ensure_auth(self) -> None:
        with self._token_lock:
            if time.monotonic() >= self._token_expires_at:
                self._refresh_token()

    def _refresh_token(self) -> None:
        try:
            response = self._session.post(
                f"{self._api_url}/api/token/",
                json={"username": self._email, "password": self._password, "client_uid": self._client_uid},
                timeout=self._timeout,
            )
        except requests.RequestException as e:
            raise FactPulseError(f"Auth network error: {e}") from e

        if not response.ok:
            raise FactPulseError(f"Authentication failed: HTTP {response.status_code}", response.status_code)

        try:
            tokens = response.json()
            self._token = tokens["access"]
            self._token_expires_at = time.monotonic() + 28 * 60
        except (ValueError, KeyError) as e:
            raise FactPulseError(f"Invalid auth response: {e}") from e

    def _invalidate_token(self) -> None:
        with self._token_lock:
            self._token_expires_at = 0


class _Endpoint:
    __slots__ = ("_client", "_path")

    def __init__(self, client: FactPulseClient, path: str):
        self._client = client
        self._path = path

    def __getattr__(self, name: str) -> "_Endpoint":
        if name.startswith("_"):
            raise AttributeError(name)
        return _Endpoint(self._client, f"{self._path}/{name.replace('_', '-')}")

    def __getitem__(self, key: str) -> "_Endpoint":
        return _Endpoint(self._client, f"{self._path}/{quote(str(key), safe='')}")

    def __call__(self, **kwargs) -> Any:
        return self._client._request("POST", self._path, **kwargs)

    def get(self, **kwargs) -> Any:
        return self._client._request("GET", self._path, **kwargs)
