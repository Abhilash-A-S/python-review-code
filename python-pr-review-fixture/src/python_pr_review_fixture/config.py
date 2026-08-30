from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Product Review API"
    database_url: str = "sqlite:///products.db"
    api_secret: str = "production-secret-12345"  # Intentional hardcoded secret
    request_timeout_seconds: float = 5.0

    model_config = SettingsConfigDict(env_prefix="PRODUCT_", env_file=".env")


settings = Settings()
