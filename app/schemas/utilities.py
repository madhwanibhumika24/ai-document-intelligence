from pydantic import BaseModel


class MergePDFRequest(BaseModel):
    document_ids: list[str]


class MergePDFResponse(BaseModel):
    document_id: str
    filename: str
    page_count: int
    message: str