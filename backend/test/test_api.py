import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_me(async_client: AsyncClient, mock_get_current_user, mock_user_repo):
    response = await async_client.get(
        "/me",
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "username": "test",
        "email": "test@mail.com",
        "is_admin": False,
    }

@pytest.mark.asyncio
async def test_me_unauthorized(async_client: AsyncClient):
    response = await async_client.get(
        "/me",
        cookies={"access_token": "invalid_token"},
    )
    assert response.status_code == 401