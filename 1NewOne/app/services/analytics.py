# 1NewOne/app/services/analytics.py
import pandas as pd

class AnalyticsService:
    def __init__(self, orders):
        self.orders = orders

    def calculate_total_sales(self):
        """Рассчитать общую сумму продаж."""
        df = pd.DataFrame(self.orders)
        return df["price"].sum()

    def get_top_products(self, n=10):
        """Получить топ-N товаров по продажам."""
        df = pd.DataFrame(self.orders)
        return df.groupby("product_name")["price"].sum().nlargest(n).to_dict()