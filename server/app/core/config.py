from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    BOT_TOKEN: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    DEBUG : bool
    AI_PROVIDER : str
    AI_BASE_URL : str
    AI_MODEL: str 
    AI_API_KEY :  str
    AI_TIMEOUT_SECONDS : float
    AI_MAX_RETRIES :  int
    AI_MAX_OUTPUT_TOKENS : int
    MAX_UPLOAD_BYTES : int
    MAX_PDF_PAGES : int
    MAX_TEXT_CHARS :int
    MAX_DOCX_UNCOMPRESSED_BYTES : int

    class Config:
        env_file = ".env"


settings = Settings()
