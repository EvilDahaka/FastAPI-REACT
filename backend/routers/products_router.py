from database import get_session
from fastapi import APIRouter, Depends, HTTPException, Request
from repositories.repo_product import ProductRepositories as repo_product
from schemas.product import ProductBase

router = APIRouter(tags=["Products"])

@router.get("/products")
async def get_products(request: Request, session=Depends(get_session)):
    repo = repo_product(session)
    products = await repo.get_products()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return {"products": products}

@router.get("/products/{product_id}")
async def get_product(product_id: int, request: Request, session=Depends(get_session)):
    repo = repo_product(session)
    product = await repo.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products")
async def create_product(product: ProductBase, request: Request, session=Depends(get_session)):
    repo = repo_product(session)
    await repo.create_product(product)
    return {"message": "Product created successfully"}

@router.put("/products/{product_id}")
async def update_product(
    product_id: int, product: ProductBase, request: Request, session=Depends(get_session)
):
    repo = repo_product(session)
    existing_product = await repo.get_product(product_id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    await repo.update_product(product_id, product)
    return {"message": "Product updated successfully"}

@router.delete("/products/{product_id}")
async def delete_product(product_id: int, request: Request, session=Depends(get_session)):
    repo = repo_product(session)
    existing_product = await repo.get_product(product_id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    await repo.delete_product(product_id)
    return {"message": "Product deleted successfully"}

@router.get("/catalogs/{catalog_id}")
async def get_catalog(catalog_id: int, request: Request, session=Depends(get_session)):
    repo = repo_product(session)
    catalog = await repo.get_catalog_by_id(catalog_id)
    products = await repo.get_catalog(catalog_id)
    if not catalog:
        raise HTTPException(status_code=404, detail="No catalogs found")
    return {"catalog": catalog, "products": products}

@router.get("/catalogs")
async def get_catalogs(request: Request, session=Depends(get_session)):
    repo = repo_product(session)
    catalogs = await repo.get_catalogs()
    if not catalogs:
        raise HTTPException(status_code=404, detail="No catalogs found")
    return {"catalogs": catalogs}