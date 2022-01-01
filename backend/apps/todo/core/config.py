from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM Stack"
    DEBUG_MODE: bool = False
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"

class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000

class DatabaseSettings(BaseSettings):
    DB_URL: str = "localhost"
    DB_NAME: str = "my_db"

class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass

settings = Settings()