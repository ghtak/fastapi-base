from fastapi import Depends
from configs.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import (
    select,
    delete
)
from sqlalchemy.orm import (
    selectinload,
    defer
)
from typing import (
    Optional,
    List
)
from entities.user_image import UserImage


class UserImageRepository:

    def __init__(self,
                 async_session: AsyncSession = Depends(get_session)):
        self.async_session = async_session

    async def images(self, user_id: Optional[int] = None) -> List[UserImage]:
        query = select(UserImage)
        if user_id:
            query = query.where(UserImage.user_id == user_id)

        result = await self.async_session.execute(query)
        return result.scalars().all()

    async def images_ids(self, user_id: Optional[int] = None) -> List[UserImage]:
        query = select(UserImage).options(
            selectinload(UserImage.user),
            defer('image'))
        if user_id:
            query = query.where(UserImage.user_id == user_id)

        result = await self.async_session.execute(query)
        return result.scalars().all()

    async def create(self, user_image: UserImage):
        self.async_session.add(user_image)
        await self.async_session.commit()
        await self.async_session.refresh(user_image)

    async def delete(self, user_image_id):
        await self.async_session.execute(
            delete(UserImage).where(UserImage.id == user_image_id))
        await self.async_session.commit()
