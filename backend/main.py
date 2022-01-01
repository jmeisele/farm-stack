import uvicorn
from fastapi import FastAPI

from apps.todo.core.config import settings
from apps.todo.core.event_handlers import start_app_handler, stop_app_handler
from apps.todo.routes.router import api_router


def app_factory() -> FastAPI:
    """
    FastAPI factory pattern

    Returns:
        FastAPI: Our app
    """
    fast_app = FastAPI(title=settings.APP_NAME, version=settings.VERSION, debug=settings.DEBUG_MODE)
    fast_app.include_router(api_router, prefix=settings.API_PREFIX)
    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))
    
    return fast_app

app = app_factory()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG_MODE,
    )