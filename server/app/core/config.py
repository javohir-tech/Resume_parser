from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    BOT_TOKEN: str
    JWT_SECRET: str
    JWT_ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()
