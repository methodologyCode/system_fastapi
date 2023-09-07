from fastapi import APIRouter, status

from managers.user import UserManager
from schemas.request.user import UserRegisterIn, UserLoginIn
from schemas.response.user import UserOut

router = APIRouter(tags=["Auth"])


@router.post("/register/",
             status_code=status.HTTP_201_CREATED,
             response_model=UserOut)
async def register(user_data: UserRegisterIn):
    user = await UserManager.register(user_data.dict())
    return user


@router.post("/login/", status_code=status.HTTP_200_OK)
async def login(user_data: UserLoginIn):
    token, role = await UserManager.login(user_data.dict())
    return {"token": token, "role": role}