from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession
)
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite+aiosqlite:///database.db'

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


# Depends(get_session)
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
