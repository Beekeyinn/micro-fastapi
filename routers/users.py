from fastapi import APIRouter, Depends, Request, Response, status

from apps.user.models import UserModel
from apps.user.schema import UserModelSerializer
from core.dependencies import ShopifyAPIDeependencies

user_router = APIRouter(dependencies=[Depends(ShopifyAPIDeependencies())])


@user_router.get("/list")
async def get_all_users(request: Request, response: Response):
    if request.state.is_authenticated:
        users = UserModel.all()
        return {
            "data": {
                "users": await UserModelSerializer.from_queryset(users),
            }
        }
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"detail": "Unauthorized Access"}
