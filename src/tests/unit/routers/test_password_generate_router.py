import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_generate_password(mocked_client: AsyncClient):
    async with mocked_client as client:
        response = await client.post("/api/v1/passwords/generate/", json={})

    assert response.status_code == 200
    assert response.json() == {"password": "something"}


@pytest.mark.asyncio
async def test_generate_password_but_input_is_not_valid(mocked_client: AsyncClient):
    async with mocked_client as client:
        response = await client.post("/api/v1/passwords/generate/", data={})

    assert response.status_code == 422
