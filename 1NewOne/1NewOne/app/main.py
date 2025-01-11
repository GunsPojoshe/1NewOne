# 1NewOne/app/main.py
from fastapi import FastAPI
from app.routers import dashboard

app = FastAPI()

# Подключаем маршруты
app.include_router(dashboard.router)

@app.get("/")
async def root():
    return {"message": "Добро пожаловать в панель управления продажами!"}