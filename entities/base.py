from sqlalchemy.ext.declarative import declarative_base
from configs.database import engine

Base = declarative_base()


async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
