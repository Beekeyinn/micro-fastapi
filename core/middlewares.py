from fastapi import Request, Response, exceptions, status
from starlette.middleware.base import BaseHTTPMiddleware


# from base import settings


class CustomMiddleware(BaseHTTPMiddleware):
    def __init__(self, app) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> None:
        # Before route handler

        response: Response = await call_next(request)

        # After view
        return response
