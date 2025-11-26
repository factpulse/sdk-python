"""
FactPulse Helpers - Client simplifié avec authentification JWT et polling intégrés.

Ce module fournit :
- FactPulseClient : Client avec auth JWT et polling automatique
- ChorusProCredentials / AFNORCredentials : Dataclasses pour le mode Zero-Trust
- Helpers montants : montant(), montant_total(), ligne_de_poste(), ligne_de_tva()

Example:
    >>> from factpulse_helpers import (
    ...     FactPulseClient,
    ...     ChorusProCredentials,
    ...     AFNORCredentials,
    ...     montant_total,
    ...     ligne_de_poste,
    ... )
    >>>
    >>> client = FactPulseClient(
    ...     email="user@example.com",
    ...     password="password",
    ...     chorus_credentials=ChorusProCredentials(
    ...         piste_client_id="...",
    ...         piste_client_secret="...",
    ...         chorus_pro_login="...",
    ...         chorus_pro_password="..."
    ...     )
    ... )
"""
from .client import (
    FactPulseClient,
    ChorusProCredentials,
    AFNORCredentials,
    montant,
    montant_total,
    ligne_de_poste,
    ligne_de_tva,
)
from .exceptions import (
    FactPulseError,
    FactPulseAuthError,
    FactPulsePollingTimeout,
    FactPulseValidationError,
    ValidationErrorDetail,
)

__all__ = [
    # Client principal
    "FactPulseClient",
    # Credentials
    "ChorusProCredentials",
    "AFNORCredentials",
    # Helpers montants
    "montant",
    "montant_total",
    "ligne_de_poste",
    "ligne_de_tva",
    # Exceptions
    "FactPulseError",
    "FactPulseAuthError",
    "FactPulsePollingTimeout",
    "FactPulseValidationError",
    "ValidationErrorDetail",
]


# Alias pour rétrocompatibilité
def format_montant(value) -> str:
    """Formate un montant pour l'API FactPulse. Alias de montant()."""
    return montant(value)
