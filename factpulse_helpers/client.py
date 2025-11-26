"""
Client FactPulse avec authentification JWT et polling intégrés.

Ce client encapsule le SDK généré automatiquement et offre une API simplifiée
avec gestion automatique de l'authentification et du polling.
"""

import time
import base64
import logging
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Optional, Dict, Any, Union
import json

import requests

from factpulse import ApiClient, Configuration
from factpulse.api import TraitementFactureApi, ChorusProApi
from factpulse.exceptions import ApiException

from .exceptions import (
    FactPulseAuthError,
    FactPulsePollingTimeout,
    FactPulseValidationError,
)

logger = logging.getLogger(__name__)


class FactPulseClient:
    """
    Client FactPulse avec authentification JWT et polling intégrés.

    Ce client :
    - Gère automatiquement l'obtention du token JWT via email/password
    - Rafraîchit le token si nécessaire
    - Gère le polling des tâches asynchrones avec backoff exponentiel
    - Intercepte les erreurs 401 et re-authentifie automatiquement

    Args:
        email: Email du compte FactPulse
        password: Mot de passe du compte
        api_url: URL de base de l'API (défaut: https://factpulse.fr)
        client_uid: Client UID optionnel pour accéder aux credentials d'un client spécifique
        polling_interval: Intervalle initial de polling en secondes (défaut: 2)
        polling_timeout: Timeout maximum pour le polling en secondes (défaut: 120)
        max_retries: Nombre maximum de tentatives en cas d'erreur 401 (défaut: 1)

    Example:
        >>> client = FactPulseClient(
        ...     email="user@example.com",
        ...     password="password"
        ... )
        >>> pdf_bytes = client.generer_facturx(facture_data, pdf_source, sync=True)
    """

    DEFAULT_API_URL = "https://factpulse.fr"
    DEFAULT_POLLING_INTERVAL = 2
    DEFAULT_POLLING_TIMEOUT = 120

    def __init__(
        self,
        email: str,
        password: str,
        api_url: str = None,
        client_uid: str = None,
        polling_interval: int = None,
        polling_timeout: int = None,
        max_retries: int = 1,
    ):
        self.email = email
        self.password = password
        self.api_url = (api_url or self.DEFAULT_API_URL).rstrip("/")
        self.client_uid = client_uid
        self.polling_interval = polling_interval or self.DEFAULT_POLLING_INTERVAL
        self.polling_timeout = polling_timeout or self.DEFAULT_POLLING_TIMEOUT
        self.max_retries = max_retries

        self._access_token: Optional[str] = None
        self._refresh_token: Optional[str] = None
        self._token_expires_at: Optional[datetime] = None

        self._api_client: Optional[ApiClient] = None

    # =========================================================================
    # Authentification
    # =========================================================================

    def _obtain_token(self) -> Dict[str, str]:
        """
        Obtient un nouveau token JWT via l'API /api/token/.

        Returns:
            Dict contenant 'access' et 'refresh' tokens

        Raises:
            FactPulseAuthError: En cas d'erreur d'authentification
        """
        token_url = f"{self.api_url}/api/token/"

        payload = {
            "username": self.email,
            "password": self.password,
        }

        if self.client_uid:
            payload["client_uid"] = self.client_uid

        try:
            response = requests.post(
                token_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=30,
            )
            response.raise_for_status()

            data = response.json()
            logger.info(
                "Token JWT obtenu pour %s (client_uid: %s)",
                self.email,
                self.client_uid or "none",
            )
            return data

        except requests.RequestException as e:
            logger.error("Erreur lors de l'obtention du token JWT: %s", e)
            raise FactPulseAuthError(f"Impossible d'obtenir le token JWT: {e}")

    def _refresh_access_token(self) -> str:
        """
        Rafraîchit le token d'accès en utilisant le refresh token.

        Returns:
            Nouveau access token

        Raises:
            FactPulseAuthError: En cas d'erreur de refresh
        """
        if not self._refresh_token:
            raise FactPulseAuthError("Aucun refresh token disponible")

        refresh_url = f"{self.api_url}/api/token/refresh/"

        try:
            response = requests.post(
                refresh_url,
                json={"refresh": self._refresh_token},
                headers={"Content-Type": "application/json"},
                timeout=30,
            )
            response.raise_for_status()

            data = response.json()
            logger.info("Token d'accès rafraîchi avec succès")
            return data["access"]

        except requests.RequestException as e:
            logger.warning("Refresh token échoué, ré-obtention d'un nouveau token: %s", e)
            return self._obtain_token()["access"]

    def _ensure_authenticated(self, force_refresh: bool = False) -> None:
        """
        S'assure que le client a un token valide.

        Args:
            force_refresh: Force le rafraîchissement du token
        """
        now = datetime.now()

        if (
            force_refresh
            or not self._access_token
            or not self._token_expires_at
            or now >= self._token_expires_at
        ):
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

    def _get_api_client(self) -> ApiClient:
        """
        Retourne un client API configuré avec le token JWT.
        """
        self._ensure_authenticated()

        config = Configuration(host=f"{self.api_url}/api/facturation")
        config.access_token = self._access_token

        self._api_client = ApiClient(configuration=config)
        return self._api_client

    def _reset_auth(self) -> None:
        """Réinitialise l'authentification pour forcer un nouveau login."""
        self._access_token = None
        self._refresh_token = None
        self._token_expires_at = None
        self._api_client = None
        logger.info("Authentification réinitialisée")

    # =========================================================================
    # APIs
    # =========================================================================

    @property
    def traitement_api(self) -> TraitementFactureApi:
        """Retourne l'API de traitement de factures."""
        return TraitementFactureApi(api_client=self._get_api_client())

    @property
    def chorus_pro_api(self) -> ChorusProApi:
        """Retourne l'API Chorus Pro."""
        return ChorusProApi(api_client=self._get_api_client())

    # =========================================================================
    # Polling
    # =========================================================================

    def poll_task(
        self,
        task_id: str,
        timeout: int = None,
        interval: int = None,
    ) -> Dict[str, Any]:
        """
        Effectue un polling sur une tâche asynchrone jusqu'à ce qu'elle soit terminée.

        Utilise un backoff exponentiel pour éviter de surcharger l'API.

        Args:
            task_id: ID de la tâche à surveiller
            timeout: Timeout en secondes (défaut: self.polling_timeout)
            interval: Intervalle initial en secondes (défaut: self.polling_interval)

        Returns:
            Résultat de la tâche une fois terminée

        Raises:
            FactPulsePollingTimeout: Si le timeout est atteint
            ApiException: Si une erreur survient lors du polling
        """
        timeout = timeout or self.polling_timeout
        interval = interval or self.polling_interval
        start_time = time.time()
        current_interval = interval

        logger.info("Début du polling pour la tâche %s (timeout: %ds)", task_id, timeout)

        while True:
            elapsed = time.time() - start_time

            if elapsed > timeout:
                raise FactPulsePollingTimeout(task_id, timeout)

            try:
                statut = self.traitement_api.obtenir_statut_tache_api_v1_traitement_taches_id_tache_statut_get(
                    id_tache=task_id
                )

                logger.info(
                    "Tâche %s: statut=%s (%.1fs écoulées)",
                    task_id,
                    statut.statut,
                    elapsed,
                )

                if statut.statut in ("completed", "SUCCESS"):
                    logger.info("Tâche %s terminée avec succès", task_id)
                    return statut.resultat

                elif statut.statut in ("failed", "FAILURE"):
                    error_msg = getattr(statut, "erreur", "Erreur inconnue")
                    logger.error("Tâche %s échouée: %s", task_id, error_msg)

                    # Extraire les erreurs de validation si présentes
                    errors = []
                    if hasattr(statut, "resultat") and statut.resultat:
                        errors = statut.resultat.get("erreurs", [])

                    raise FactPulseValidationError(
                        f"La tâche {task_id} a échoué: {error_msg}",
                        errors=errors,
                    )

                # Backoff exponentiel (max 10 secondes)
                time.sleep(current_interval)
                current_interval = min(current_interval * 1.5, 10)

            except ApiException as e:
                if e.status == 401:
                    logger.warning("Token expiré pendant le polling, re-authentification...")
                    self._reset_auth()
                    continue
                raise

    # =========================================================================
    # Méthodes de haut niveau
    # =========================================================================

    def _call_with_retry(self, func, *args, **kwargs):
        """
        Appelle une fonction API avec retry automatique en cas de 401.
        """
        for attempt in range(self.max_retries + 1):
            try:
                return func(*args, **kwargs)
            except ApiException as e:
                if e.status == 401 and attempt < self.max_retries:
                    logger.warning(
                        "Erreur 401, réinitialisation du token (tentative %d/%d)",
                        attempt + 1,
                        self.max_retries + 1,
                    )
                    self._reset_auth()
                    continue
                raise

    def generer_facturx(
        self,
        facture_data: Union[Dict, str],
        pdf_source: bytes,
        profil: str = "EN16931",
        format_sortie: str = "pdf",
        sync: bool = True,
        timeout: int = None,
    ) -> Union[bytes, str]:
        """
        Génère une facture Factur-X.

        Args:
            facture_data: Données de la facture (dict ou JSON string)
            pdf_source: PDF source en bytes
            profil: Profil Factur-X (MINIMUM, BASIC, EN16931, EXTENDED)
            format_sortie: Format de sortie (pdf ou xml)
            sync: Si True, attend le résultat (polling). Sinon retourne le task_id.
            timeout: Timeout pour le polling en secondes

        Returns:
            Si sync=True: bytes du PDF/XML généré
            Si sync=False: task_id (string)

        Raises:
            FactPulseValidationError: En cas d'erreur de validation
            FactPulsePollingTimeout: Si le timeout est atteint
        """
        # Convertir dict en JSON si nécessaire
        if isinstance(facture_data, dict):
            facture_data = json.dumps(facture_data, default=self._json_serializer)

        def _call():
            return self.traitement_api.generer_facture_api_v1_traitement_generer_facture_post(
                donnees_facture=facture_data,
                profil=profil,
                format_sortie=format_sortie,
                source_pdf=pdf_source,
            )

        response = self._call_with_retry(_call)
        task_id = response.id_tache

        if not sync:
            return task_id

        # Polling et récupération du résultat
        resultat = self.poll_task(task_id, timeout=timeout)

        if resultat and resultat.get("statut") == "ERREUR":
            raise FactPulseValidationError(
                resultat.get("message_erreur", "Erreur de validation"),
                errors=resultat.get("erreurs", []),
            )

        if resultat and "contenu_b64" in resultat:
            return base64.b64decode(resultat["contenu_b64"])

        raise FactPulseValidationError("Le résultat ne contient pas de contenu")

    def valider_facturx(
        self,
        pdf_source: bytes,
        sync: bool = True,
        timeout: int = None,
    ) -> Union[Dict, str]:
        """
        Valide un PDF Factur-X existant.

        Args:
            pdf_source: PDF Factur-X à valider
            sync: Si True, attend le résultat. Sinon retourne le task_id.
            timeout: Timeout pour le polling

        Returns:
            Si sync=True: dict avec le résultat de validation
            Si sync=False: task_id (string)
        """
        def _call():
            return self.traitement_api.valider_facturx_api_v1_traitement_valider_facturx_post(
                fichier=pdf_source,
            )

        response = self._call_with_retry(_call)
        task_id = response.id_tache

        if not sync:
            return task_id

        return self.poll_task(task_id, timeout=timeout)

    @staticmethod
    def _json_serializer(obj):
        """Sérialiseur JSON pour les types non standard."""
        if isinstance(obj, Decimal):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    # =========================================================================
    # Helpers pour les montants
    # =========================================================================

    @staticmethod
    def format_montant(montant: Union[Decimal, float, int, str]) -> str:
        """
        Formate un montant pour l'API FactPulse.

        L'API accepte number, string ou integer, mais string est recommandé
        pour préserver la précision des montants monétaires.

        Args:
            montant: Montant à formater

        Returns:
            String formatée avec 2 décimales minimum

        Example:
            >>> FactPulseClient.format_montant(1234.5)
            '1234.50'
            >>> FactPulseClient.format_montant(Decimal('1234.10'))
            '1234.10'
        """
        if montant is None:
            return "0.00"
        if isinstance(montant, str):
            montant = Decimal(montant)
        elif isinstance(montant, (int, float)):
            montant = Decimal(str(montant))
        return f"{montant:.2f}"
