# app/routers/integrations.py
from fastapi import APIRouter
from app.api.wildberries import WildberriesAPI
from app.api.ozon import OzonAPI

router = APIRouter()

@router.get("/integrations/wildberries/orders")
async def get_wildberries_orders():
    """
    Получить заказы с Wildberries.
    
    :return: Список заказов с Wildberries.
    """
    wb_api = WildberriesAPI()
    return wb_api.get_orders()

@router.get("/integrations/ozon/orders")
async def get_ozon_orders():
    """
    Получить заказы с Ozon.
    
    :return: Список заказов с Ozon.
    """
    ozon_api = OzonAPI()
    return ozon_api.get_orders()