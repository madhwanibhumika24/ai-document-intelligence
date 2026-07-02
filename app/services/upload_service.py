from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile

from app.core.config import settings
from app.schemas.upload import UploadResponse


class UploadService:
    async def save(self, file: UploadFile) -> UploadResponse:
        # 1. Validate file
        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed."
            )

        # 2. Generate unique identifiers
        document_id = str(uuid4())

        extension = Path(file.filename).suffix

        stored_filename = f"{document_id}{extension}"

        # 3. Storage path
        upload_dir = Path(settings.UPLOAD_DIRECTORY)

        upload_dir.mkdir(parents=True, exist_ok=True)

        file_path = upload_dir / stored_filename

        # 4. Read uploaded file
        contents = await file.read()

        # 5. Save file
        with open(file_path, "wb") as buffer:
            buffer.write(contents)

        # 6. Return response
        return UploadResponse(
            document_id=document_id,
            filename=file.filename,
            stored_filename=stored_filename,
            content_type=file.content_type,
            size=len(contents),
            message="Document uploaded successfully.",
        )