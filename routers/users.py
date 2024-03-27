from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.responses import JSONResponse

from apps.user.models import UserModel
from apps.user.schema import UserModelSerializer
from core.dependencies import ShopifyAPIDeependencies

user_router = APIRouter(dependencies=[Depends(ShopifyAPIDeependencies())])


@user_router.get("/list")
async def get_all_users(request: Request, response: Response):
    if request.state.is_authenticated:
        users = UserModel.all()
        return JSONResponse(
            content={
                "data": {
                    "users": await UserModelSerializer.from_queryset(users),
                },
            },
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            content={"detail": "Unauthorized Access"},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
