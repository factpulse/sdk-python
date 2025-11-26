"""
FactPulse Helpers - Client simplifié avec authentification JWT et polling intégrés.
"""
from .client import FactPulseClient
from .exceptions import (
    FactPulseError,
    FactPulseAuthError,
    FactPulsePollingTimeout,
    FactPulseValidationError,
    ValidationErrorDetail,
)

__all__ = [
    "FactPulseClient",
    "FactPulseError",
    "FactPulseAuthError",
    "FactPulsePollingTimeout",
    "FactPulseValidationError",
    "ValidationErrorDetail",
]


def format_montant(montant) -> str:
    """Formate un montant pour l'API FactPulse."""
    return FactPulseClient.format_montant(montant)
