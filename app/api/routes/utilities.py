from fastapi import APIRouter, status

from app.schemas.utilities import MergePDFRequest, MergePDFResponse
from app.services.pdf_utility_service import PDFUtilityService

router = APIRouter(
    prefix="/documents",
    tags=["PDF Utilities"],
)

pdf_utility_service = PDFUtilityService()


@router.post(
    "/merge",
    response_model=MergePDFResponse,
    status_code=status.HTTP_201_CREATED,
)
async def merge_pdfs(request: MergePDFRequest):
    return pdf_utility_service.merge(request)