from fastapi import APIRouter, Request, Response

from ..controllers.users.users_controller import GetAllUsersController

user_router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"]
)


@user_router.get(path='/')
async def getAll() -> dict[str, str]:
    return GetAllUsersController.handle()
