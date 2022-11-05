from fastapi import (
    APIRouter,
    Depends,
    status
)
from typing import List
from dtos.user_dto import (
    UserBaseDto,
    UserDto
)
from usecases.user_usecase import UserUsecase
from usecases.token import verify

user_router = APIRouter(
    prefix='/v1/user',
    dependencies=[Depends(verify)]
)


@user_router.get('/', tags=['user'],
                 response_model=List[UserDto])
async def get(
        user_usecase: UserUsecase = Depends()
):
    return await user_usecase.users()


@user_router.post('/',
                  response_model=UserDto,
                  status_code=status.HTTP_201_CREATED
                  )
async def create(
        user_base_dto: UserBaseDto,
        user_usecase: UserUsecase = Depends()
):
    return await user_usecase.create(user_base_dto)


@user_router.patch('/{id}',
                   response_model=UserDto)
async def update(
        id: int,
        user: UserBaseDto,
        user_usecase: UserUsecase = Depends()
):
    return await user_usecase.update(id, user)


@user_router.delete('/{id}',
                    status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        id: int,
        user_usecase: UserUsecase = Depends()
):
    return await user_usecase.delete(id)
