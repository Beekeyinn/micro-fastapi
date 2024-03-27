from fastapi import Request
from shopify import session_token

from apps.shopify.models import ShopifySession
from base import settings


def authorization_header(request: Request):
    return request.headers.get("authorization")


class ShopifyAPIDeependencies:

    async def __call__(self, request: Request) -> None:
        if getattr(settings, "DEBUG") and "/docs" in request.headers.get("referer"):
            user = await ShopifySession.get(shop=getattr(settings, "ADMIN_DOMAIN"))
            request.state.is_authenticated = True
            request.state.user = user
        else:
            try:
                decoded_session_token = await self.is_shopify_request(request)
                shopify_domain = decoded_session_token.get("dest").removeprefix(
                    "https://"
                )
                user = ShopifySession.get(shop=shopify_domain)
            except Exception:
                request.state.is_authenticated = False
                request.state.user = None

            else:
                request.state.user = user
                request.state.is_authenticated = True

    async def is_shopify_request(self, request: Request):
        decoded_session_token = session_token.decode_from_header(
            authorization_header=authorization_header(request),
            api_key=getattr(settings, "SHOPIFY_API_KEY"),
            secret=getattr(settings, "SHOPIFY_API_SECRET"),
        )
        return decoded_session_token
