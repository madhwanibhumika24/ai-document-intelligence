from pathlib import Path
from uuid import uuid4

from pypdf import PdfReader, PdfWriter

from app.core.config import settings
from app.schemas.registry import DocumentMetadata
from app.schemas.utilities import MergePDFRequest, MergePDFResponse
from app.services.registry_service import RegistryService


class PDFUtilityService:

    def __init__(self):
        self.registry_service = RegistryService()

    def merge(self, request: MergePDFRequest) -> MergePDFResponse:

        writer = PdfWriter()
        total_pages = 0

        for document_id in request.document_ids:

            document = self.registry_service.get_document(document_id)

            if document is None:
                raise ValueError(f"Document {document_id} not found.")

            pdf_path = document["path"]

            reader = PdfReader(pdf_path)

            total_pages += len(reader.pages)

            for page in reader.pages:
                writer.add_page(page)

        merged_document_id = str(uuid4())

        generated_dir = Path(settings.GENERATED_DIRECTORY) / "merged"
        generated_dir.mkdir(parents=True, exist_ok=True)

        merged_filename = f"{merged_document_id}.pdf"

        merged_path = generated_dir / merged_filename

        with open(merged_path, "wb") as output_file:
            writer.write(output_file)

        self.registry_service.add_document(
            DocumentMetadata(
                document_id=merged_document_id,
                filename="Merged.pdf",
                stored_filename=merged_filename,
                path=str(merged_path),
                content_type="application/pdf",
                size=merged_path.stat().st_size,
            )
        )

        return MergePDFResponse(
            document_id=merged_document_id,
            filename=merged_filename,
            page_count=total_pages,
            message="PDFs merged successfully."
        )