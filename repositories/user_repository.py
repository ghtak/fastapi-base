from fastapi import Depends
from configs.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from entities.user import User


class UserRepository:

    def __init__(self,
                 async_session: AsyncSession = Depends(get_session)):
        self.async_session = async_session

    async def users(self):
        result = await self.async_session.execute(
            select(User))
        return result.scalars().all()
