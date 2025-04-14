import asyncio


from database import engine
from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class UserModel(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False)

    @classmethod
    def from_schema(cls, schema: BaseModel) -> "UserModel":
        return cls(**schema.model_dump())
    
class ProductModel(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[float] = mapped_column(nullable=False)
    image: Mapped[bytes] = mapped_column(nullable=True)

    catalog_id: Mapped[int] = mapped_column(ForeignKey("catalogs.id"), nullable=False)
    catalog: Mapped["CatalogModel"] = relationship("CatalogModel", back_populates="products")

class CatalogModel(Base):
    __tablename__ = "catalogs"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    image: Mapped[bytes] = mapped_column(nullable=True)

    # Відношення до ProductModel
    products: Mapped[list["ProductModel"]] = relationship("ProductModel", back_populates="catalog")

    @classmethod
    def from_schema(cls, schema: BaseModel) -> "CatalogModel":
        return cls(**schema.model_dump())

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(init_db())