from fastapi import APIRouter, Request

from .models import UserModel
from .schema import UserModelSerializer

user_router = APIRouter()


@user_router.get("/list")
async def get_all_users(request: Request):
    users = UserModel.all()
    return {
        "data": {
            "users": await UserModelSerializer.from_queryset(users),
        }
    }
