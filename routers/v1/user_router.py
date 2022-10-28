from fastapi import APIRouter, Depends
from typing import List
from dtos.userdto import UserDto

user_router = APIRouter(
    prefix='/v1/user'
)


@user_router.get('/', tags=['user'], response_model=List[UserDto])
async def get():
    return [UserDto(
        id=0, name='user'
    )]
