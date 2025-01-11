# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Настройки для Wildberries API
    wildberries_api_key: str
    wildberries_base_url: str = "https://suppliers-api.wildberries.ru"

    # Настройки для Ozon API
    ozon_api_key: str
    ozon_client_id: str
    ozon_base_url: str = "https://api-seller.ozon.ru"

    # Настройки базы данных
    database_url: str = "sqlite:///./sales.db"

    class Config:
        env_file = ".env"

settings = Settings()