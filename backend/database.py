import asyncio
import logging

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

PATH_DATABASE = "data/database.db"
engine = create_async_engine(f"sqlite+aiosqlite:///{PATH_DATABASE}")

new_session = async_sessionmaker(bind=engine, expire_on_commit=False)

log = logging.getLogger(__name__)

async def get_session():
    async with new_session() as session:
        yield session

class Base(DeclarativeBase):
    pass


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        log.info("Database initialized")


if __name__ == "__main__":
    asyncio.run(init_db())