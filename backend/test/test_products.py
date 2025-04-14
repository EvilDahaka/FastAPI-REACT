import pytest
from httpx import AsyncClient
from fastapi import status
from unittest.mock import AsyncMock

# filepath: d:\webApp\FastAPI-REACT\backend\routers\test_products_router.py

@pytest.fixture
def mock_repo_product(mocker):
    """Mock the ProductRepositories class."""
    mock_repo = mocker.patch("routers.products_router.repo_product", autospec=True)
    return mock_repo

@pytest.mark.asyncio
async def test_get_products_success(mock_repo_product, async_client: AsyncClient):
    mock_repo_product.return_value.get_products = AsyncMock(return_value=[{"id": 1, "name": "Product 1"}])

    response = await async_client.get("/products")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"products": [{"id": 1, "name": "Product 1"}]}

@pytest.mark.asyncio
async def test_get_products_not_found(mock_repo_product, async_client: AsyncClient):
    mock_repo_product.return_value.get_products = AsyncMock(return_value=[])

    response = await async_client.get("/products")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "No products found"}

@pytest.mark.asyncio
async def test_get_product_success(mock_repo_product, async_client: AsyncClient):
    mock_repo_product.return_value.get_product = AsyncMock(return_value={"id": 1, "name": "Product 1"})

    response = await async_client.get("/products/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"id": 1, "name": "Product 1"}

@pytest.mark.asyncio
async def test_get_product_not_found(mock_repo_product, async_client: AsyncClient):
    mock_repo_product.return_value.get_product = AsyncMock(return_value=None)

    response = await async_client.get("/products/1")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Product not found"}

@pytest.mark.asyncio
async def test_create_product_success(mock_repo_product, async_client: AsyncClient):
    mock_repo_product.return_value.create_product = AsyncMock()

    product_data = {"name": "New Product", "price": 100}
    response = await async_client.post("/products", json=product_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Product created successfully"}

@pytest.mark.asyncio
async def test_update_product_success(mock_repo_product, async_client: AsyncClient):
    mock_repo_product.return_value.get_product = AsyncMock(return_value={"id": 1, "name": "Product 1"})