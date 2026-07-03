from pydantic import BaseModel


class UploadResponse(BaseModel):
    document_id: str
    filename: str
    stored_filename: str
    content_type: str
    size: int
    message: str


class MultipleUploadResponse(BaseModel):
    documents: list[UploadResponse]