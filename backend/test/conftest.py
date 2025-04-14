from unittest.mock import AsyncMock, patch

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from main import app


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client

@pytest_asyncio.fixture
async def async_client_with_cookies(async_client):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        # Set up cookies or any other session data here
        await client.get("/login", cookies={"access_token": "your_token_here"})
        yield client

@pytest_asyncio.fixture
async def mock_get_current_user():
    with patch("routers.user.get_current_user", new_callable=AsyncMock) as mock_user:
        mock_user.return_value = {"id": 1}
        yield mock_user

@pytest_asyncio.fixture
async def mock_user_repo():
    with patch("routers.user.user_repo") as mock_repo_class:
        # Mock the instance of user_repo
        mock_repo_instance = AsyncMock()
        mock_repo_instance.get_user = AsyncMock(
            return_value={
                "id": 1,
                "username": "test",
                "email": "test@mail.com",  # Valid email address
                "is_admin": False,  # Include all required fields
        })
        mock_repo_class.return_value = mock_repo_instance
        yield mock_repo_instance