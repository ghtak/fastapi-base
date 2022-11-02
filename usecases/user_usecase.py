from fastapi import Depends
from repositories.user_repository import UserRepository
from dtos.user_dto import (
    UserBaseDto,
    UserDto
)
from entities.user import User


class UserUsecase:

    def __init__(self,
                 user_repo: UserRepository = Depends()):
        self.user_repo = user_repo

    async def users(self):
        return [
            UserDto(id=u.id, name=u.name) for u in await self.user_repo.users()
        ]

    async def create(self, user_base_dto: UserBaseDto) -> UserDto:
        u = await self.user_repo.create(
            User(name=user_base_dto.name)
        )
        return UserDto(id=u.id, name=u.name)

    async def update(self, user_id: int, user_base_dto: UserBaseDto) -> UserDto:
        u = await self.user_repo.update(
            User(id=user_id, name=user_base_dto.name)
        )
        return UserDto(id=u.id, name=u.name)

    async def delete(self, user_id: int):
        return await self.user_repo.delete(user_id)