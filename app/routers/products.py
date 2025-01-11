# app/routers/products.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.models import Product

router = APIRouter()

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products/")
async def get_products(db: Session = Depends(get_db)):
    """
    Получить список всех продуктов.
    
    :param db: Сессия базы данных.
    :return: Список продуктов.
    """
    products = db.query(Product).all()
    return products

@router.get("/products/{product_id}")
async def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Получить информацию о конкретном продукте.
    
    :param product_id: ID продукта.
    :param db: Сессия базы данных.
    :return: Информация о продукте.
    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    return product