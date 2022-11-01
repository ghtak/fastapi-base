from fastapi import Depends
from configs.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload, defer
from entities.user_image import UserImage
from typing import Optional


class UserImageRepository:

    def __init__(self,
                 async_session: AsyncSession = Depends(get_session)):
        self.async_session = async_session

    async def images(self, user_id: Optional[int] = None):
        query = select(UserImage)
        if user_id:
            query = query.where(UserImage.user_id == user_id)

        result = await self.session.execute(query)
        return result.scalars().all()

    async def images_ids(self, user_id: Optional[int] = None):
        query = select(UserImage).options(
            selectinload(UserImage.user),
            defer('image'))
        if user_id:
            query = query.where(UserImage.user_id == user_id)

        result = await self.session.execute(query)
        return result.scalars().all()