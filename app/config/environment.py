from typing import Any
from pydantic import BaseSettings
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv('../.env'))


class Settings(BaseSettings):    
    DB_HOST: Any = os.environ.get("DB_HOST") #"localhost"
    DB_PORT: int = int(os.environ.get("DB_PORT")) 
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DIALECT: str = os.environ.get("DIALECT")


settings = Settings()
