from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from base.settings import settings


def setup(app: FastAPI):
    register_tortoise(app, config=settings.DATABASES)
    handle_cors(app)


def register_database(app):
    register_tortoise(app, config=settings.DATABASES)


def handle_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=getattr(settings, "CORS_ALLOW_ORIGINS", ["*"]),
        allow_credentials=getattr(settings, "CORS_ALLOW_CREDENTIALS", True),
        allow_methods=getattr(settings, "CORS_ALLOW_METHODS", ["*"]),
        allow_headers=getattr(settings, "CORS_ALLOW_HEADERS", ["*"]),
    )
