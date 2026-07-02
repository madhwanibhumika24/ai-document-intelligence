from fastapi import APIRouter

from app.core.config import settings
from app.schemas.status import RootResponse, HealthResponse

router = APIRouter(tags=["Status"])


@router.get("/", response_model=RootResponse)
def root():
    return RootResponse(
        app=settings.APP_NAME,
        version=settings.APP_VERSION,
        status="running",
    )


@router.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(
        status="healthy",
    )