from fastapi import APIRouter, Depends
from typing import List
from dtos.userdto import UserDto
from usecases.user_usecase import UserUsecase


user_router = APIRouter(
    prefix='/v1/user'
)


@user_router.get('/', tags=['user'], response_model=List[UserDto])
async def get(
        user_usecase: UserUsecase = Depends()
):
    return await user_usecase.users()
