import re

import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    [
        'password_length',
        'has_numbers',
        'has_lowercase_chars',
        'has_uppercase_chars',
        'has_special_chars',
        'expected_match',
    ],
    [
        (20, True, False, False, False, r'^\d+$'),
        (20, False, True, False, False, r'^[a-z]+$'),
        (25, False, False, True, False, r'^[A-Z]+$'),
        (1, False, False, False, True, r'^[!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]+$'),
        (15, True, True, True, True, r'^[a-zA-Z0-9!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]+$'),
    ],
)
@pytest.mark.asyncio
async def test_e2e_generate_password(
    mocked_client: AsyncClient,
    password_length: int,
    has_numbers: bool,
    has_lowercase_chars: bool,
    has_uppercase_chars: bool,
    has_special_chars: bool,
    expected_match: str,
):

    async with mocked_client as client:
        response = await client.post(
            "/api/v1/passwords/generate/",
            json={
                "password_length": password_length,
                "has_numbers": has_numbers,
                "has_lowercase_chars": has_lowercase_chars,
                "has_uppercase_chars": has_uppercase_chars,
                "has_special_chars": has_special_chars,
            }
        )

    assert response.status_code == 200
    body = response.json()
    assert body['password'] is not None
    assert len(body['password']) == password_length
    assert re.match(pattern=expected_match, string=body['password'])
