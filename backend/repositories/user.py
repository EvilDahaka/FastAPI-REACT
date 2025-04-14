import logging
import select
from schemas.users import UserModel

from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

log = logging.getLogger(__name__)

class UserRepositories:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        
    async def get_by_email(self, email: str) -> UserModel | None:
        stmt = select(UserModel).where(UserModel.email == email)
        result = await self.session.execute(stmt)
        log.debug(result)
        return result.scalar_one_or_none()
    
    async def get_user(self, uid: str):
        stmt = select(UserModel).where(UserModel.id == int(uid))
        result = await self.session.execute(stmt)
        return result.scalar_one()