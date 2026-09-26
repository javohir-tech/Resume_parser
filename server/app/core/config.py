from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    BOT_TOKEN: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    DEBUG: bool
    
    AI_PROVIDER: str
    AI_BASE_URL: str
    AI_MODEL: str
    AI_API_KEY: str

    AI_TIMEOUT_SECONDS: float = 60
    AI_MAX_RETRIES: int = 1
    AI_MAX_OUTPUT_TOKENS: int = 8192

    MAX_UPLOAD_BYTES: int = 10 * 1024 * 1024
    MAX_PDF_PAGES: int = 10
    MAX_TEXT_CHARS: int = 40_000
    MAX_DOCX_UNCOMPRESSED_BYTES: int = 50 * 1024 * 1024

    class Config:
        env_file = ".env"


settings = Settings()
