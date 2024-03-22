from base import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise


def setup(app: FastAPI):
    register_tortoise(app, config=settings.DATABASES)


def register_database(app):
    register_tortoise(app, config=settings.DATABASES)


def handle_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=getattr(settings, "ALLOW_ORIGINS", ["*"]),
        allow_credentials=getattr(settings, "ALLOW_CREDENTIALS", True),
        allow_methods=getattr(settings, "ALLOW_METHODS", ["*"]),
        allow_headers=getattr(settings, "ALLOW_HEADERS", ["*"]),
    )
