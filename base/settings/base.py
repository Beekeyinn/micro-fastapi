from pathlib import Path

from dotenv import load_dotenv

SECRET_KEY = "test"

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR)
MODEL_APPS = []

DATABASES = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.postgresql",
            "credentials": {
                "name": "",
                "user": "",
                "password": "",
                "host": "",
                "port": "",
            },
        }
    },
    "apps": {
        "models": [f"apps.{app}.models" for app in MODEL_APPS],
    },
}
