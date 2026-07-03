from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile

from app.core.config import settings
from app.schemas.registry import DocumentMetadata
from app.schemas.upload import UploadResponse, MultipleUploadResponse
from app.services.registry_service import RegistryService


class UploadService:

    def __init__(self):
        self.registry_service = RegistryService()

    async def save(
        self,
        files: list[UploadFile],
    ) -> MultipleUploadResponse:

        uploaded_documents = []

        upload_dir = Path(settings.UPLOAD_DIRECTORY)
        upload_dir.mkdir(parents=True, exist_ok=True)

        for file in files:

            # Validate file
            if file.content_type != "application/pdf":
                raise HTTPException(
                    status_code=400,
                    detail=f"{file.filename} is not a PDF."
                )

            # Generate unique ID
            document_id = str(uuid4())

            extension = Path(file.filename).suffix
            stored_filename = f"{document_id}{extension}"

            file_path = upload_dir / stored_filename

            # Read uploaded file
            contents = await file.read()

            if not contents:
                raise HTTPException(
                    status_code=400,
                    detail=f"{file.filename} is empty."
                )

            # Save file
            with open(file_path, "wb") as buffer:
                buffer.write(contents)

            # Register document
            self.registry_service.add_document(
                DocumentMetadata(
                    document_id=document_id,
                    filename=file.filename,
                    stored_filename=stored_filename,
                    path=str(file_path),
                    content_type=file.content_type,
                    size=len(contents),
                )
            )

            # Prepare response
            uploaded_documents.append(
                UploadResponse(
                    document_id=document_id,
                    filename=file.filename,
                    stored_filename=stored_filename,
                    content_type=file.content_type,
                    size=len(contents),
                    message="Document uploaded successfully."
                )
            )

        return MultipleUploadResponse(
            documents=uploaded_documents
        )