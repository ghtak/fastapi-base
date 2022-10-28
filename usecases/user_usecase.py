from fastapi import Depends
from repositories.user_repository import UserRepository
from dtos.userdto import UserDto


class UserUsecase:

    def __init__(self,
                 user_repo: UserRepository = Depends()):
        self.user_repo = user_repo

    async def users(self):
        return [
            UserDto(id=u.id, name=u.name) for u in await self.user_repo.users()
        ]
