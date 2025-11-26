"""Client simplifié pour l'API FactPulse avec authentification JWT et polling intégrés."""
import base64
import json
import logging
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

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


# =============================================================================
# Credentials dataclasses - pour une configuration simplifiée
# =============================================================================

@dataclass
class ChorusProCredentials:
    """Credentials Chorus Pro pour le mode Zero-Trust.

    Ces credentials sont passés dans chaque requête et ne sont jamais stockés côté serveur.

    Attributes:
        piste_client_id: Client ID PISTE (portail API gouvernement)
        piste_client_secret: Client Secret PISTE
        chorus_pro_login: Login Chorus Pro
        chorus_pro_password: Mot de passe Chorus Pro
        sandbox: True pour l'environnement sandbox, False pour production
    """
    piste_client_id: str
    piste_client_secret: str
    chorus_pro_login: str
    chorus_pro_password: str
    sandbox: bool = True

    def to_dict(self) -> Dict[str, Any]:
        """Convertit en dictionnaire pour l'API."""
        return {
            "piste_client_id": self.piste_client_id,
            "piste_client_secret": self.piste_client_secret,
            "chorus_pro_login": self.chorus_pro_login,
            "chorus_pro_password": self.chorus_pro_password,
            "sandbox": self.sandbox,
        }


@dataclass
class AFNORCredentials:
    """Credentials AFNOR PDP pour le mode Zero-Trust.

    Ces credentials sont passés dans chaque requête et ne sont jamais stockés côté serveur.

    Attributes:
        client_id: Client ID OAuth2 de la PDP
        client_secret: Client Secret OAuth2 de la PDP
        flow_service_url: URL du Flow Service de la PDP
    """
    client_id: str
    client_secret: str
    flow_service_url: str

    def to_dict(self) -> Dict[str, Any]:
        """Convertit en dictionnaire pour l'API."""
        return {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "flow_service_url": self.flow_service_url,
        }


# =============================================================================
# Helpers pour les types anyOf - évite la verbosité des wrappers générés
# =============================================================================

def montant(value: Union[str, float, int, Decimal, None]) -> str:
    """Convertit une valeur en string de montant pour l'API.

    L'API FactPulse accepte les montants comme strings ou floats.
    Cette fonction normalise en string pour garantir la précision monétaire.
    """
    if value is None:
        return "0.00"
    if isinstance(value, Decimal):
        return f"{value:.2f}"
    if isinstance(value, (int, float)):
        return f"{value:.2f}"
    if isinstance(value, str):
        return value
    return "0.00"


def montant_total(
    ht: Union[str, float, int, Decimal],
    tva: Union[str, float, int, Decimal],
    ttc: Union[str, float, int, Decimal],
    a_payer: Union[str, float, int, Decimal],
    remise_ttc: Union[str, float, int, Decimal, None] = None,
    motif_remise: Optional[str] = None,
    acompte: Union[str, float, int, Decimal, None] = None,
) -> Dict[str, Any]:
    """Crée un objet MontantTotal simplifié.

    Évite d'avoir à utiliser les wrappers MontantHtTotal, MontantTvaTotal, etc.
    """
    result = {
        "montantHtTotal": montant(ht),
        "montantTva": montant(tva),
        "montantTtcTotal": montant(ttc),
        "montantAPayer": montant(a_payer),
    }
    if remise_ttc is not None:
        result["montantRemiseGlobaleTtc"] = montant(remise_ttc)
    if motif_remise is not None:
        result["motifRemiseGlobaleTtc"] = motif_remise
    if acompte is not None:
        result["acompte"] = montant(acompte)
    return result


def ligne_de_poste(
    numero: int,
    denomination: str,
    quantite: Union[str, float, int, Decimal],
    montant_unitaire_ht: Union[str, float, int, Decimal],
    montant_ligne_ht: Union[str, float, int, Decimal],
    taux_tva: Union[str, float, int, Decimal] = "20.00",
    categorie_tva: str = "S",
    unite: str = "C62",
    reference: Optional[str] = None,
    montant_tva_ligne: Union[str, float, int, Decimal, None] = None,
    montant_remise_ht: Union[str, float, int, Decimal, None] = None,
    code_raison_reduction: Optional[str] = None,
    raison_reduction: Optional[str] = None,
    motif_exoneration: Optional[str] = None,
    date_debut_periode: Optional[str] = None,
    date_fin_periode: Optional[str] = None,
    description: Optional[str] = None,
    reference_acheteur: Optional[str] = None,
    reference_vendeur: Optional[str] = None,
) -> Dict[str, Any]:
    """Crée une ligne de poste simplifiée.

    Args:
        numero: Numéro de la ligne
        denomination: Libellé du produit/service
        quantite: Quantité
        montant_unitaire_ht: Prix unitaire HT
        montant_ligne_ht: Total ligne HT
        taux_tva: Taux de TVA (défaut: "20.00")
        categorie_tva: Catégorie TVA - S (standard), Z (zéro), E (exonéré), AE (autoliquidation), K (intracommunautaire)
        unite: Code unité UN/ECE (défaut: "C62" = unité)
        reference: Référence article vendeur
        montant_tva_ligne: Montant TVA de la ligne (optionnel)
        montant_remise_ht: Montant de remise HT (optionnel)
        code_raison_reduction: Code raison de la réduction (ex: "95" = remise)
        raison_reduction: Description textuelle de la réduction
        motif_exoneration: Code motif d'exonération TVA (ex: "VATEX-EU-AE")
        date_debut_periode: Date début période de facturation (YYYY-MM-DD)
        date_fin_periode: Date fin période de facturation (YYYY-MM-DD)
        description: Description détaillée
        reference_acheteur: Référence article côté acheteur
        reference_vendeur: Référence article côté vendeur
    """
    result = {
        "numero": numero,
        "denomination": denomination,
        "quantite": montant(quantite),
        "montantUnitaireHt": montant(montant_unitaire_ht),
        "montantTotalLigneHt": montant(montant_ligne_ht),
        "tauxTva": montant(taux_tva),
        "categorieTva": categorie_tva,
        "unite": unite,
    }
    if reference is not None:
        result["reference"] = reference
    if montant_tva_ligne is not None:
        result["montantTvaLigne"] = montant(montant_tva_ligne)
    if montant_remise_ht is not None:
        result["montantRemiseHt"] = montant(montant_remise_ht)
    if code_raison_reduction is not None:
        result["codeRaisonReduction"] = code_raison_reduction
    if raison_reduction is not None:
        result["raisonReduction"] = raison_reduction
    if motif_exoneration is not None:
        result["motifExoneration"] = motif_exoneration
    if date_debut_periode is not None:
        result["dateDebutPeriode"] = date_debut_periode
    if date_fin_periode is not None:
        result["dateFinPeriode"] = date_fin_periode
    if description is not None:
        result["description"] = description
    if reference_acheteur is not None:
        result["referenceArticleAcheteur"] = reference_acheteur
    if reference_vendeur is not None:
        result["referenceArticleVendeur"] = reference_vendeur
    return result


def ligne_de_tva(
    taux: Union[str, float, int, Decimal],
    base_ht: Union[str, float, int, Decimal],
    montant_tva: Union[str, float, int, Decimal],
    categorie: str = "S",
    motif_exoneration: Optional[str] = None,
) -> Dict[str, Any]:
    """Crée une ligne de TVA simplifiée."""
    result = {
        "tauxTva": montant(taux),
        "montantBaseHt": montant(base_ht),
        "montantTva": montant(montant_tva),
        "categorieTva": categorie,
    }
    if motif_exoneration is not None:
        result["motifExoneration"] = motif_exoneration
    return result


class FactPulseClient:
    """Client simplifié pour l'API FactPulse.

    Gère l'authentification JWT, le polling des tâches asynchrones,
    et permet de configurer les credentials Chorus Pro / AFNOR à l'initialisation.
    """

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
        chorus_credentials: Optional[ChorusProCredentials] = None,
        afnor_credentials: Optional[AFNORCredentials] = None,
        polling_interval: Optional[int] = None,
        polling_timeout: Optional[int] = None,
        max_retries: Optional[int] = None,
    ):
        self.email = email
        self.password = password
        self.api_url = (api_url or self.DEFAULT_API_URL).rstrip("/")
        self.client_uid = client_uid
        self.chorus_credentials = chorus_credentials
        self.afnor_credentials = afnor_credentials
        self.polling_interval = polling_interval or self.DEFAULT_POLLING_INTERVAL
        self.polling_timeout = polling_timeout or self.DEFAULT_POLLING_TIMEOUT
        self.max_retries = max_retries if max_retries is not None else self.DEFAULT_MAX_RETRIES

        self._access_token: Optional[str] = None
        self._refresh_token: Optional[str] = None
        self._token_expires_at: Optional[datetime] = None
        self._api_client: Optional[ApiClient] = None

    def get_chorus_credentials_for_api(self) -> Optional[Dict[str, Any]]:
        """Retourne les credentials Chorus Pro au format API."""
        return self.chorus_credentials.to_dict() if self.chorus_credentials else None

    def get_afnor_credentials_for_api(self) -> Optional[Dict[str, Any]]:
        """Retourne les credentials AFNOR au format API."""
        return self.afnor_credentials.to_dict() if self.afnor_credentials else None

    # Alias plus courts pour faciliter l'usage
    def get_chorus_pro_credentials(self) -> Optional[Dict[str, Any]]:
        """Alias pour get_chorus_credentials_for_api()."""
        return self.get_chorus_credentials_for_api()

    def get_afnor_credentials(self) -> Optional[Dict[str, Any]]:
        """Alias pour get_afnor_credentials_for_api()."""
        return self.get_afnor_credentials_for_api()

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
