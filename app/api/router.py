from fastapi import APIRouter

from app.api.health.router import router as health_router

# Все эндпоинты доступны только по префиксу `/api`
api_router = APIRouter(prefix="/api")
api_router.include_router(health_router)
