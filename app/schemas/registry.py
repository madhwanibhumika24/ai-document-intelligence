from pydantic import BaseModel


class DocumentMetadata(BaseModel):
    document_id: str
    filename: str
    stored_filename: str
    path: str
    content_type: str
    size: int