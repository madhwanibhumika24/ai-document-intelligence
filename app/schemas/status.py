from pydantic import BaseModel


class RootResponse(BaseModel):
    app: str
    version: str
    status: str


class HealthResponse(BaseModel):
    status: str