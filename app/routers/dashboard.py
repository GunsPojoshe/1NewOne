# app/routers/dashboard.py
from fastapi import APIRouter
from app.api.wildberries import WildberriesAPI
from app.api.ozon import OzonAPI
from app.services.analytics import AnalyticsService

router = APIRouter()

@router.get("/dashboard")
async def get_dashboard():
    """Получить данные для главной страницы."""
    # Получаем данные от Wildberries
    wb_api = WildberriesAPI()
    wb_orders = wb_api.get_orders()

    # Получаем данные от Ozon
    ozon_api = OzonAPI()
    ozon_orders = ozon_api.get_orders()

    # Анализируем данные
    analytics = AnalyticsService(wb_orders + ozon_orders)
    total_sales = analytics.calculate_total_sales()
    top_products = analytics.get_top_products()

    return {
        "total_sales": total_sales,
        "top_products": top_products,
    }