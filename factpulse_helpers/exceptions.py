"""
Exceptions personnalisées pour le client FactPulse.
"""


class FactPulseError(Exception):
    """Classe de base pour toutes les erreurs FactPulse."""

    pass


class FactPulseAuthError(FactPulseError):
    """Erreur d'authentification (credentials invalides, token expiré, etc.)."""

    pass


class FactPulsePollingTimeout(FactPulseError):
    """Timeout lors du polling d'une tâche asynchrone."""

    def __init__(self, task_id: str, timeout: int, message: str = None):
        self.task_id = task_id
        self.timeout = timeout
        super().__init__(
            message or f"Timeout ({timeout}s) atteint pour la tâche {task_id}"
        )


class FactPulseValidationError(FactPulseError):
    """Erreur de validation Factur-X (Schematron, BR-FR, etc.)."""

    def __init__(self, message: str, errors: list = None):
        self.errors = errors or []
        super().__init__(message)

    def __str__(self):
        if self.errors:
            error_messages = "\n".join(
                f"  - [{e.get('item', 'unknown')}] {e.get('reason', e.get('message', 'Unknown error'))}"
                for e in self.errors
            )
            return f"{super().__str__()}\n\nDétails:\n{error_messages}"
        return super().__str__()
