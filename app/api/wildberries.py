import requests
from app.core.config import settings

class WildberriesAPI:
    def __init__(self):
        self.base_url = settings.wildberries_base_url
        self.api_key = settings.wildberries_api_key

    def get_orders(self) -> list:
        """
        Получить список заказов с Wildberries.
        
        :return: Список заказов.
        """
        url = f"{self.base_url}/api/v1/orders"
        headers = {"Authorization": self.api_key}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_stock(self) -> list:
        """
        Получить информацию о остатках на складе Wildberries.
        
        :return: Список остатков.
        """
        url = f"{self.base_url}/api/v1/stocks"
        headers = {"Authorization": self.api_key}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()