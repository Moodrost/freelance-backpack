from app.core.config import settings


def get_health_status() -> str:
    """Return application health status."""
    return settings.default.health_status
