from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class CustomMiddleware(BaseHTTPMiddleware):
    def __init__(self, app) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> None:
        # Before route handler
        print("CUSTOM Middleware Before: request method", request.method)

        response: Response = await call_next(request)

        # After view
        print("CUSTOM Middleware After: response status", response.status_code)
        return response
