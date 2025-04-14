import logging

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

PATH_DATABASE = "data/database.db"
engine = create_async_engine(f"sqlite+aiosqlite:///{PATH_DATABASE}")

new_session = async_sessionmaker(bind=engine, expire_on_commit=False)

log = logging.getLogger(__name__)

async def get_session():
    async with new_session() as session:
        yield session