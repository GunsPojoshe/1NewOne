import pandas as pd

class AnalyticsService:
    def __init__(self, orders: list):
        """
        Инициализация сервиса аналитики.
        
        :param orders: Список заказов.
        """
        self.orders = orders

    def calculate_total_sales(self) -> float:
        """
        Рассчитать общую сумму продаж.
        
        :return: Общая сумма продаж.
        """
        df = pd.DataFrame(self.orders)
        return df["price"].sum()

    def get_top_products(self, n: int = 10) -> dict:
        """
        Получить топ-N товаров по продажам.
        
        :param n: Количество товаров для вывода.
        :return: Словарь с топ-N товарами.
        """
        df = pd.DataFrame(self.orders)
        return df.groupby("product_name")["price"].sum().nlargest(n).to_dict()