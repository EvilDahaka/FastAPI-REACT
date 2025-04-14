from typing import Optional

from pydantic import BaseModel, Field


class CatalogBase(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    image: Optional[bytes] = None

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: int = Field(..., gt=0)
    image: Optional[bytes] = None

    catalog_id: Optional[int] = None