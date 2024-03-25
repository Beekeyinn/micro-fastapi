import os
from pathlib import Path

from dotenv import load_dotenv

SECRET_KEY = "test"

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")


MODEL_APPS: list[str] = ["user"]

DATABASES = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.psycopg",
            "credentials": {
                "database": os.getenv("DATABASE_NAME"),
                "user": os.getenv("DATABASE_USERNAME"),
                "password": os.getenv("DATABASE_PASSWORD"),
                "host": os.getenv("DATABASE_HOST"),
                "port": int(os.getenv("DATABASE_PORT")),
            },
        }
    },
    "apps": {
        "models": {
            "models": [f"apps.{app}.models" for app in MODEL_APPS] + ["aerich.models"],
            "default_connection": "default",
        },
    },
}

TORTOISE_ORM = DATABASES


CORS_ALLOW_ORIGINS: list = list(os.getenv("CORS_ALLOWED_ORIGIN", ["*"]))
CORS_ALLOWED_METHODS: list = list(os.getenv("CORS_ALLOWED_METHODS", ["*"]))
CORS_ALLOWED_HEADERS: list = list(os.getenv("CORS_ALLOWED_HEADERS", ["*"]))
CORS_ALLOW_CREDENTIALS: bool = bool(os.getenv("CORS_ALLOW_CREDENTIALS", ["*"]))


EMAIL_USERNAME: str = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD: str = os.getenv("EMAIL_PASSWORD")
EMAIL_FROM: str = os.getenv("EMAIL_FROM")
EMAIL_PORT: int = os.getenv("EMAIL_PORT")
EMAIL_SERVER: str = os.getenv("EMAIL_SERVER")
EMAIL_FROM_NAME: str = os.getenv("EMAIL_FROM_NAME")


class Settings:
    """
    A class to hold all constant values.
    """

    def __init__(self, constants_dict):
        for key, value in constants_dict.items():
            if str(key).isupper():
                setattr(self, key, value)


constants_dict = globals()

settings = Settings(constants_dict)
