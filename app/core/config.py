from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Document Intelligence API"
    APP_VERSION: str = "1.0.0"

    UPLOAD_DIRECTORY: str = "app/storage/uploads"


settings = Settings()