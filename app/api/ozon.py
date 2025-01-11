import requests
from app.core.config import settings

class OzonAPI:
    def __init__(self):
        self.base_url = settings.ozon_base_url
        self.api_key = settings.ozon_api_key
        self.client_id = settings.ozon_client_id

    def get_orders(self) -> list:
        """
        Получить список заказов с Ozon.
        
        :return: Список заказов.
        """
        url = f"{self.base_url}/v2/posting/fbs/list"
        headers = {
            "Client-Id": self.client_id,
            "Api-Key": self.api_key,
        }
        payload = {
            "dir": "ASC",
            "filter": {},
            "limit": 10,
            "offset": 0,
        }
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    def get_stock(self) -> list:
        """
        Получить информацию о остатках на складе Ozon.
        
        :return: Список остатков.
        """
        url = f"{self.base_url}/v1/product/info/stocks"
        headers = {
            "Client-Id": self.client_id,
            "Api-Key": self.api_key,
        }
        payload = {
            "page": 1,
            "page_size": 100,
        }
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()