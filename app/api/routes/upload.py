from fastapi import APIRouter, File, UploadFile, status

from app.schemas.upload import MultipleUploadResponse
from app.services.upload_service import UploadService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

upload_service = UploadService()


@router.post(
    "/upload",
    response_model=MultipleUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_documents(
    files: list[UploadFile] = File(...)
):
    return await upload_service.save(files)