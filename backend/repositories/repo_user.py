import logging
import select
from typing import Optional
from models import UserModel

from schemas.users import UserOut


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
    
    async def get_user(self, uid: str) -> UserOut:
        stmt = select(UserModel).where(UserModel.id == int(uid))
        result = await self.session.execute(stmt)
        user = result.scalar_one()
        result = UserOut.validate(user)
        return result
    
    async def create_user(self, email: str, password: str, username: Optional[str] = None):
        user = UserModel(
            username=username,  # Provide a default username if None
            email=email,
            password=password,
            is_admin=False,
        )
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)