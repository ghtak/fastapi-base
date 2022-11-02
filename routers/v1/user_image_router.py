from fastapi import (
    APIRouter,
    Depends,
    status
)
from dtos.user_image_dto import (
    UserImageBaseDto,
    UserImageDto
)
from typing import List
from usecases.user_image_usecase import UserImageUsecase

user_image_router = APIRouter(
    prefix='/v1/user_image'
)


@user_image_router.get('/{user_id}',
                       response_model=List[UserImageDto])
async def get(
        user_id: int,
        user_image_usecase: UserImageUsecase = Depends()
):
    return await user_image_usecase.images(user_id)


@user_image_router.post('/{user_id}',
                        status_code=status.HTTP_201_CREATED)
async def create(
        user_id: int,
        user_image_dto: UserImageBaseDto,
        user_image_usecase: UserImageUsecase = Depends()
):
    return await user_image_usecase.create(user_id, user_image_dto)
