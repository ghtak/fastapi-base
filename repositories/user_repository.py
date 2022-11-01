from fastapi import Depends
from configs.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from entities.user import User
from typing import List


class UserRepository:

    def __init__(self,
                 async_session: AsyncSession = Depends(get_session)):
        self.async_session = async_session

    async def users(self) -> List[User]:
        result = await self.async_session.execute(
            select(User))
        return result.scalars().all()

    async def create(self, user: User) -> User:
        self.async_session.add(user)
        await self.async_session.commit()
        await self.async_session.refresh(user)
        return user

    async def update(self, user: User) -> User:
        await self.async_session.merge(user)
        await self.async_session.commit()
        return user

    async def delete(self, user_id: int) -> None:
        await self.async_session.execute(
            delete(User).where(User.id == user_id))
        await self.async_session.commit()
