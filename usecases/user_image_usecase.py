from fastapi import Depends, HTTPException, status
from repositories.user_repository import UserRepository
from repositories.user_image_repository import UserImageRepository
from entities.user_image import UserImage
from dtos.user_image_dto import (
    UserImageBaseDto,
    UserImageDto
)
import base64
import numpy as np


class UserImageUsecase:
    def __init__(self,
                 user_repo: UserRepository = Depends(),
                 user_image_repo: UserImageRepository = Depends()):
        self.user_repo = user_repo
        self.user_image_repo = user_image_repo

    async def images(self, user_id: int):
        return [UserImageDto(
            user_id=ui.id,
            image=base64.encode(ui.image)
        ) for ui in await self.user_image_repo.images(user_id)]

    async def create(self, user_id: int, user_image_dto: UserImageBaseDto):
        u = await self.user_repo.get(user_id)
        if not u:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST)
        image = np.frombuffer(base64.b64decode(user_image_dto.image),
                              np.uint8)

        await self.user_image_repo.create(
            UserImage(
                user_id=user_id,
                image=image.tobytes()  # marshal.dumps()
            ))
