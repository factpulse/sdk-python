"""Client simplifié pour l'API FactPulse avec authentification JWT et polling intégrés."""
import base64
import json
import logging
import time
from datetime import datetime, timedelta
from decimal import Decimal
from pathlib import Path
from typing import Any, Dict, Optional, Union

import requests

import factpulse
from factpulse import ApiClient, Configuration, TraitementFactureApi

from .exceptions import (
    FactPulseAuthError,
    FactPulsePollingTimeout,
    FactPulseValidationError,
    ValidationErrorDetail,
)

logger = logging.getLogger(__name__)


class FactPulseClient:
    """Client simplifié pour l'API FactPulse."""

    DEFAULT_API_URL = "https://factpulse.fr"
    DEFAULT_POLLING_INTERVAL = 2000  # ms
    DEFAULT_POLLING_TIMEOUT = 120000  # ms
    DEFAULT_MAX_RETRIES = 1

    def __init__(
        self,
        email: str,
        password: str,
        api_url: Optional[str] = None,
        client_uid: Optional[str] = None,
        polling_interval: Optional[int] = None,
        polling_timeout: Optional[int] = None,
        max_retries: Optional[int] = None,
    ):
        self.email = email
        self.password = password
        self.api_url = (api_url or self.DEFAULT_API_URL).rstrip("/")
        self.client_uid = client_uid
        self.polling_interval = polling_interval or self.DEFAULT_POLLING_INTERVAL
        self.polling_timeout = polling_timeout or self.DEFAULT_POLLING_TIMEOUT
        self.max_retries = max_retries if max_retries is not None else self.DEFAULT_MAX_RETRIES

        self._access_token: Optional[str] = None
        self._refresh_token: Optional[str] = None
        self._token_expires_at: Optional[datetime] = None
        self._api_client: Optional[ApiClient] = None

    def _obtain_token(self) -> Dict[str, str]:
        """Obtient un nouveau token JWT."""
        token_url = f"{self.api_url}/api/token/"
        payload = {"username": self.email, "password": self.password}
        if self.client_uid:
            payload["client_uid"] = self.client_uid

        try:
            response = requests.post(token_url, json=payload, timeout=30)
            response.raise_for_status()
            logger.info("Token JWT obtenu pour %s", self.email)
            return response.json()
        except requests.RequestException as e:
            error_detail = ""
            if hasattr(e, "response") and e.response is not None:
                try:
                    error_detail = e.response.json().get("detail", str(e))
                except Exception:
                    error_detail = str(e)
            raise FactPulseAuthError(f"Impossible d'obtenir le token JWT: {error_detail or e}")

    def _refresh_access_token(self) -> str:
        """Rafraîchit le token d'accès."""
        if not self._refresh_token:
            raise FactPulseAuthError("Aucun refresh token disponible")

        refresh_url = f"{self.api_url}/api/token/refresh/"
        try:
            response = requests.post(
                refresh_url, json={"refresh": self._refresh_token}, timeout=30
            )
            response.raise_for_status()
            logger.info("Token rafraîchi avec succès")
            return response.json()["access"]
        except requests.RequestException:
            logger.warning("Refresh échoué, ré-obtention d'un nouveau token")
            tokens = self._obtain_token()
            self._refresh_token = tokens["refresh"]
            return tokens["access"]

    def ensure_authenticated(self, force_refresh: bool = False) -> None:
        """S'assure que le client est authentifié."""
        now = datetime.now()

        if force_refresh or not self._access_token or not self._token_expires_at or now >= self._token_expires_at:
            if self._refresh_token and self._token_expires_at and not force_refresh:
                try:
                    self._access_token = self._refresh_access_token()
                    self._token_expires_at = now + timedelta(minutes=28)
                    return
                except FactPulseAuthError:
                    pass

            tokens = self._obtain_token()
            self._access_token = tokens["access"]
            self._refresh_token = tokens["refresh"]
            self._token_expires_at = now + timedelta(minutes=28)

    def reset_auth(self) -> None:
        """Réinitialise l'authentification."""
        self._access_token = None
        self._refresh_token = None
        self._token_expires_at = None
        self._api_client = None
        logger.info("Authentification réinitialisée")

    def get_traitement_api(self) -> TraitementFactureApi:
        """Retourne l'API de traitement de factures."""
        self.ensure_authenticated()
        config = Configuration(host=f"{self.api_url}/api/facturation")
        config.access_token = self._access_token
        self._api_client = ApiClient(configuration=config)
        return TraitementFactureApi(api_client=self._api_client)

    def poll_task(self, task_id: str, timeout: Optional[int] = None, interval: Optional[int] = None) -> Dict[str, Any]:
        """Effectue un polling sur une tâche jusqu'à son achèvement."""
        timeout_ms = timeout or self.polling_timeout
        interval_ms = interval or self.polling_interval

        start_time = time.time() * 1000
        current_interval = float(interval_ms)

        logger.info("Début du polling pour la tâche %s (timeout: %dms)", task_id, timeout_ms)

        while True:
            elapsed = (time.time() * 1000) - start_time

            if elapsed > timeout_ms:
                raise FactPulsePollingTimeout(task_id, timeout_ms)

            try:
                api = self.get_traitement_api()
                statut = api.obtenir_statut_tache_api_v1_traitement_taches_id_tache_statut_get(id_tache=task_id)

                status_value = statut.statut.value if hasattr(statut.statut, "value") else str(statut.statut)
                logger.info("Tâche %s: statut=%s (%.0fms)", task_id, status_value, elapsed)

                if status_value == "SUCCESS":
                    logger.info("Tâche %s terminée avec succès", task_id)
                    if statut.resultat:
                        if hasattr(statut.resultat, "to_dict"):
                            return statut.resultat.to_dict()
                        return dict(statut.resultat)
                    return {}

                if status_value == "FAILURE":
                    error_msg = "Erreur inconnue"
                    errors = []
                    if statut.resultat:
                        result = statut.resultat.to_dict() if hasattr(statut.resultat, "to_dict") else dict(statut.resultat)
                        error_msg = result.get("message_erreur", error_msg)
                        for err in result.get("erreurs", []):
                            errors.append(ValidationErrorDetail(
                                level=err.get("level", ""),
                                item=err.get("item", ""),
                                reason=err.get("reason", ""),
                                source=err.get("source"),
                                code=err.get("code"),
                            ))
                    raise FactPulseValidationError(f"La tâche {task_id} a échoué: {error_msg}", errors)

            except FactPulseValidationError:
                raise
            except Exception as e:
                if "401" in str(e):
                    logger.warning("Token expiré, re-authentification...")
                    self.reset_auth()
                    continue
                raise FactPulseValidationError(f"Erreur API: {e}")

            time.sleep(current_interval / 1000)
            current_interval = min(current_interval * 1.5, 10000)

    def generer_facturx(
        self,
        facture_data: Union[Dict, str],
        pdf_source: Union[bytes, str, Path],
        profil: str = "EN16931",
        format_sortie: str = "pdf",
        sync: bool = True,
        timeout: Optional[int] = None,
    ) -> bytes:
        """Génère une facture Factur-X."""
        if isinstance(facture_data, dict):
            json_data = json.dumps(facture_data)
        else:
            json_data = facture_data

        if isinstance(pdf_source, (str, Path)):
            pdf_bytes = Path(pdf_source).read_bytes()
        else:
            pdf_bytes = pdf_source

        task_id = None
        for attempt in range(self.max_retries + 1):
            try:
                api = self.get_traitement_api()
                response = api.generer_facture_api_v1_traitement_generer_facture_post(
                    donnees_facture=json_data,
                    profil=profil,
                    format_sortie=format_sortie,
                    source_pdf=pdf_bytes,
                )
                task_id = response.id_tache
                break
            except Exception as e:
                if "401" in str(e) and attempt < self.max_retries:
                    logger.warning("Erreur 401, réinitialisation du token (tentative %d/%d)", attempt + 1, self.max_retries + 1)
                    self.reset_auth()
                    continue
                raise FactPulseValidationError(f"Erreur API: {e}")

        if not task_id:
            raise FactPulseValidationError("Pas d'ID de tâche dans la réponse")

        if not sync:
            return task_id.encode()

        result = self.poll_task(task_id, timeout)

        if result.get("statut") == "ERREUR":
            error_msg = result.get("message_erreur", "Erreur de validation")
            errors = [
                ValidationErrorDetail(
                    level=e.get("level", ""),
                    item=e.get("item", ""),
                    reason=e.get("reason", ""),
                    source=e.get("source"),
                    code=e.get("code"),
                )
                for e in result.get("erreurs", [])
            ]
            raise FactPulseValidationError(error_msg, errors)

        if "contenu_b64" in result:
            return base64.b64decode(result["contenu_b64"])

        raise FactPulseValidationError("Le résultat ne contient pas de contenu")

    @staticmethod
    def format_montant(montant) -> str:
        """Formate un montant pour l'API FactPulse."""
        if montant is None:
            return "0.00"
        if isinstance(montant, Decimal):
            return f"{montant:.2f}"
        if isinstance(montant, (int, float)):
            return f"{montant:.2f}"
        if isinstance(montant, str):
            return montant
        return "0.00"
