"""
FactPulse Helpers - Client simplifié avec authentification et polling intégrés.

Ce module fournit une couche d'abstraction au-dessus du SDK généré automatiquement,
offrant :
- Authentification JWT automatique avec refresh
- Polling des tâches asynchrones avec backoff exponentiel
- Gestion des erreurs 401 avec re-authentification
- Conversion automatique des types (Decimal, dates)

Usage:
    from factpulse_helpers import FactPulseClient

    client = FactPulseClient(
        email="user@example.com",
        password="password",
        api_url="https://factpulse.fr"
    )

    # Génération synchrone (polling automatique)
    pdf_bytes = client.generer_facturx(facture_data, pdf_source, sync=True)
"""

from .client import FactPulseClient
from .exceptions import (
    FactPulseError,
    FactPulseAuthError,
    FactPulsePollingTimeout,
    FactPulseValidationError,
)

__all__ = [
    "FactPulseClient",
    "FactPulseError",
    "FactPulseAuthError",
    "FactPulsePollingTimeout",
    "FactPulseValidationError",
]

__version__ = "1.0.0"
