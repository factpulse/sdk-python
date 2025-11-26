"""Exceptions personnalisées pour le client FactPulse."""
from dataclasses import dataclass, field
from typing import List, Optional


class FactPulseError(Exception):
    """Classe de base pour toutes les erreurs FactPulse."""
    pass


class FactPulseAuthError(FactPulseError):
    """Erreur d'authentification FactPulse."""
    pass


class FactPulsePollingTimeout(FactPulseError):
    """Timeout lors du polling d'une tâche asynchrone."""
    def __init__(self, task_id: str, timeout: int):
        self.task_id = task_id
        self.timeout = timeout
        super().__init__(f"Timeout ({timeout}ms) atteint pour la tâche {task_id}")


@dataclass
class ValidationErrorDetail:
    """Détail d'une erreur de validation au format AFNOR."""
    level: str = ""
    item: str = ""
    reason: str = ""
    source: Optional[str] = None
    code: Optional[str] = None

    def __str__(self) -> str:
        item = self.item or "unknown"
        reason = self.reason or "Unknown error"
        return f"[{item}] {reason}"


class FactPulseValidationError(FactPulseError):
    """Erreur de validation avec détails structurés."""
    def __init__(self, message: str, errors: List[ValidationErrorDetail] = None):
        self.errors = errors or []
        if self.errors:
            details = "\n".join(f"  - {e}" for e in self.errors)
            message = f"{message}\n\nDétails:\n{details}"
        super().__init__(message)
