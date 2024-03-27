from fastapi import Request, exceptions, status
from fastapi.responses import JSONResponse
from shopify import session_token

from apps.shopify.models import ShopifySession
from base import settings


def authorization_header(request: Request):
    header = request.headers.get("authorization", None)
    if header is None:
        raise exceptions.HTTPException(
            detail="Authorization header is required",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    return header


class ShopifyAPIDeependencies:

    async def __call__(self, request: Request) -> None:
        if getattr(settings, "DEBUG") and "/docs" in request.headers.get("referer"):
            user = await ShopifySession.get(shop=getattr(settings, "ADMIN_DOMAIN"))
            request.state.is_authenticated = True
            request.state.user = user
        else:
            decoded_session_token = await self.is_shopify_request(request)
            shopify_domain = decoded_session_token.get("dest").removeprefix("https://")
            user = ShopifySession.get(shop=shopify_domain)
            request.state.user = user
            request.state.is_authenticated = True

    async def is_shopify_request(self, request: Request):
        auth = authorization_header(request)
        try:
            decoded_session_token = session_token.decode_from_header(
                authorization_header=auth,
                api_key=getattr(settings, "SHOPIFY_API_KEY"),
                secret=getattr(settings, "SHOPIFY_API_SECRET"),
            )
        except Exception as e:
            raise exceptions.HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Invalid Shopify Token",
            )
        else:
            return decoded_session_token
