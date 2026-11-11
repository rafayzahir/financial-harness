from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Financial Harness API"
    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: str = "postgresql+psycopg://postgres:password@localhost:5432/financial_harness"

    SECRET_KEY: str = "change-this-secret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    REDIS_URL: str = "redis://localhost:6379/0"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()