from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.schemas.extraction import ExtractionResponse
from app.services.pdf_service import PDFService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

pdf_service = PDFService()


@router.post(
    "/{document_id}/extract",
    response_model=ExtractionResponse,
)
def extract_text(document_id: str):

    upload_dir = Path(settings.UPLOAD_DIRECTORY)

    pdf_files = list(upload_dir.glob(f"{document_id}.*"))

    if not pdf_files:
        raise HTTPException(
            status_code=404,
            detail="Document not found.",
        )

    return pdf_service.extract_text(
        document_id=document_id,
        file_path=pdf_files[0],
    )