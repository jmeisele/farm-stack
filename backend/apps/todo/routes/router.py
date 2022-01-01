
from fastapi import APIRouter

from apps.todo.routes import crud

api_router = APIRouter()
api_router.include_router(crud.router, tags=["CRUD"])
