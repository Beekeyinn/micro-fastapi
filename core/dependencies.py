from fastapi import Request
from shopify import session_token

from apps.shopify.models import ShopifySession
from base import settings


def authorization_header(request: Request):
    return request.headers.get("authorization")


class ShopifyAPIDeependencies:

    async def __call__(self, request: Request) -> None:
        print("headers", request.headers)
        if getattr(settings, "DEBUG") and "/docs" in request.headers.get("referer"):
            user = ShopifySession.get(shop=getattr(settings, "ADMIN_DOMAIN"))
            request.state.is_authenticated = True
            request.state.user = user
        else:
            try:
                decoded_session_token = self.is_shopify_request(request)
            except Exception as e:
                request.state.user = None

            shopify_domain = decoded_session_token.get("dest").removeprefix("https://")
            try:
                user = ShopifySession.get(shop=shopify_domain)
            except Exception:
                request.state.is_authenticated = False
                request.state.user = None

            else:
                request.state.user = user
                request.state.is_authenticated = True

    def is_shopify_request(self, request: Request):
        try:
            decoded_session_token = session_token.decode_from_header(
                authorization_header=authorization_header(request),
                api_key=getattr(settings, "SHOPIFY_API_KEY"),
                secret=getattr(settings, "SHOPIFY_API_SECRET"),
            )
        except Exception as e:
            raise exceptions.AuthenticationFailed("Requires Shopify based request.")
        else:
            return decoded_session_token
        pass
