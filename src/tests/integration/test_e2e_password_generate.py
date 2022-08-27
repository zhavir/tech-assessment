import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_e2e_generate_password(mocked_client: AsyncClient):
    expected_length = 20

    async with mocked_client as client:
        response = await client.post("/api/v1/passwords/generate/", json={
            "password_length": expected_length,
        })

    assert response.status_code == 200
    body = response.json()
    assert body['password'] is not None
    assert len(body['password']) == expected_length
