from unittest.mock import AsyncMock

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_generate_password(
    mocked_client: AsyncClient,
    mocked_password_generator_service: AsyncMock,
        mocked_randomizer_provider,
):
    mocked_password_generator_service.return_value.generate_password = AsyncMock(return_value="something")

    async with mocked_client as client:
        response = await client.post("/api/v1/passwords/generate/", json={})

    assert response.status_code == 200
    assert response.json() == {"password": "something"}


@pytest.mark.asyncio
@pytest.mark.parametrize(
    [
        'body',
    ],
    [
        ({
            "password_length": 0
        }, ),
        (
            {
                "has_special_chars": False,
                "has_uppercase_chars": False,
                "has_lowercase_chars": False,
                "has_numbers": False,
            },
        ),
    ],
)
async def test_generate_password_but_input_is_not_valid(
    mocked_client: AsyncClient,
    mocked_password_generator_service: AsyncMock,
        mocked_randomizer_provider,
    body: dict,
):
    async with mocked_client as client:
        response = await client.post("/api/v1/passwords/generate/", json=body)

    assert response.status_code == 422
