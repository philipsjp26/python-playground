from typing import Any
from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: Any = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str = "fastapi_playground"
    DB_USER: str = "root"
    DB_PASSWORD: str = ""
    DIALECT: str = "mysql+mysqldb"

settings = Settings()