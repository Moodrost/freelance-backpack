from fastapi import APIRouter

from app.services.health import get_health_status
from .schemas import HealthCheckResponse

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", response_model=HealthCheckResponse)
async def health_check() -> HealthCheckResponse:
    """Health check endpoint."""
    status = get_health_status()
    return HealthCheckResponse(status=status)
