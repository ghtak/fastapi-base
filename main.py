from fastapi import FastAPI
from entities.base import init_models
from entities.user import User
from entities.user_image import UserImage
import asyncio
from routers.v1.index_router import index_router
from routers.v1.user_router import user_router
from routers.v1.user_image_router import user_image_router

app = FastAPI()

app.include_router(index_router)
app.include_router(user_router)
app.include_router(user_image_router)

asyncio.create_task(init_models())
