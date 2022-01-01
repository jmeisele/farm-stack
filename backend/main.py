import os
from fastapi import FastAPI

from core.config import settings

from core.event_handlers import start_app_handler, stop_app_handler

def app_factory() -> FastAPI:
    """
    FastAPI factory pattern

    Returns:
        FastAPI: Our app
    """
    fast_app = FastAPI(title=settings.APP_NAME, version=settings.VERSION, debug=settings.DEBUG_MODE)
    # fast_app =.include_router(api_router, prefix=settings.API_PREFIX)
    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))
    
    return fast_app

app = app_factory()