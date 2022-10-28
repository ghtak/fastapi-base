from fastapi import FastAPI
from routers.v1.index_router import index_router
from entities.base import init_models

import asyncio

app = FastAPI()
app.include_router(index_router)

asyncio.create_task(init_models())
