from typing import Callable

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from apps.todo.core.config import settings


async def _startup_mongodb_client(app: FastAPI) -> None:
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME]

async def _shutdown_mongodb_client(app: FastAPI) -> None:
    app.mongodb_client.close()

def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        _startup_mongodb_client(app)
    
    return startup

def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        _shutdown_mongodb_client(app)
    
    return shutdown