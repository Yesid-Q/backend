import ssl

from typing import List
from pydantic import BaseSettings

# Class for personalized settings
class Settings(BaseSettings):
    DEBUG: bool
    APP_NAME: str
    DESCRIPTION: str
    VERSION: str
    SECRET_KEY: str

    DATABASE_DRIVER: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_DATABASE: str


    MODELS: List[str] = [
        'models.nation_model',
        'models.club_model',
        'models.player_model',
    ]

    class Config:
        env_file_encoding = 'utf-8'

settings = Settings()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'database': settings.DATABASE_DATABASE,
                'host': 'database',
                'password': settings.DATABASE_PASSWORD,
                'port': settings.DATABASE_PORT,
                'user': settings.DATABASE_USER,
                'ssl': 'disable' if settings.DEBUG else ctx
            }
        }
    },
    'apps': {
        'models': {
            'models': settings.MODELS,
            'default_connection': 'default',
        }
    },
    'use_tz': False,
    'timezone': 'UTC'
}