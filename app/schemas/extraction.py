from pydantic import BaseModel


class ExtractionResponse(BaseModel):
    document_id: str
    page_count: int
    character_count: int
    text: str
    extraction_engine: str
    message: str