from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from tortoise.contrib.fastapi import register_tortoise

from base.settings import settings
from core.middlewares import CustomMiddleware


def setup(app: FastAPI):
    handle_cors(app)
    register_middleware(app)
    register_database(app)


def register_database(app):
    register_tortoise(
        app,
        config=settings.DATABASES,
        generate_schemas=True,
        add_exception_handlers=True,
    )


def handle_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=getattr(settings, "CORS_ALLOW_ORIGINS", ["*"]),
        allow_credentials=getattr(settings, "CORS_ALLOW_CREDENTIALS", True),
        allow_methods=getattr(settings, "CORS_ALLOW_METHODS", ["*"]),
        allow_headers=getattr(settings, "CORS_ALLOW_HEADERS", ["*"]),
    )


def register_middleware(app: FastAPI):
    app.add_middleware(GZipMiddleware)
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)

    app.add_middleware(CustomMiddleware)
