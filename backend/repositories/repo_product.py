import select

from models import CatalogModel, ProductModel
from schemas.product import ProductBase
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession


class ProductRepositories:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_product(self, product_id) -> ProductModel | None:
        stmt = select(ProductModel).where(ProductModel.id == product_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_products(self, limit: int = 30) -> list[ProductModel]:
        stmt = select(ProductModel).order_by(func.random()).limit(limit)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def create_product(self, product: ProductBase) -> ProductModel:
        # Перетворення Pydantic-схеми в SQLAlchemy-модель
        product_model = ProductModel(**product.dict())
        self.session.add(product_model)
        await self.session.commit()
        await self.session.refresh(product_model)
        return product_model

    async def update_product(self, product_id: int, product: ProductBase) -> ProductModel | None:
        stmt = select(ProductModel).where(ProductModel.id == product_id)
        result = await self.session.execute(stmt)
        existing_product = result.scalar_one_or_none()
        if not existing_product:
            return None
        for key, value in product.dict().items():
            setattr(existing_product, key, value)
        await self.session.commit()
        await self.session.refresh(existing_product)
        return existing_product

    async def delete_product(self, product_id: int) -> bool:
        stmt = select(ProductModel).where(ProductModel.id == product_id)
        result = await self.session.execute(stmt)
        existing_product = result.scalar_one_or_none()
        if not existing_product:
            return False
        await self.session.delete(existing_product)
        await self.session.commit()
        return True

    async def get_catalogs(self) -> list[CatalogModel] | None:
        stmt = select(CatalogModel)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def get_catalog(self, catalog_id: int) -> list[ProductModel] | None:
        stmt = select(ProductModel).where(ProductModel.catalog_id == catalog_id)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

    async def get_catalog_by_id(self, catalog_id: int) -> CatalogModel | None:
        stmt = select(CatalogModel).where(CatalogModel.id == catalog_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()