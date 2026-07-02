from fastapi import APIRouter

from app.api.routes.status import router as status_router
from app.api.routes.upload import router as upload_router

api_router = APIRouter()

api_router.include_router(status_router)
api_router.include_router(upload_router)