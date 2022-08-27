from unittest.mock import AsyncMock

import pytest

from app.services.password_generator_service import PasswordGeneratorService
from app.providers.randomizer_provider import RandomizerProvider


@pytest.mark.parametrize(
    [
        'password_length',
        'has_numbers',
        'has_lowercase_chars',
        'has_uppercase_chars',
        'has_special_chars',
    ],
    [
        (100, False, False, False, False),
        (0, True, True, True, True),
        (201, False, False, False, True),
        (0, False, False, False, False),
        (201, False, False, False, False),
        (100, False, True, False, False),
    ],
)
@pytest.mark.asyncio
async def test_password_generator_service(
    password_length: int,
    has_numbers: bool,
    has_lowercase_chars: bool,
    has_uppercase_chars: bool,
    has_special_chars: bool,
):
    expected_password = "a-Password"
    mocked_randomizer_service = AsyncMock(spec_set=RandomizerProvider)
    service = PasswordGeneratorService(randomizer_service=mocked_randomizer_service)

    mocked_randomizer_service.randomize.return_value = expected_password
    result = await service.generate_password(
        password_length=10,
        has_numbers=True,
        has_lowercase_chars=True,
        has_uppercase_chars=True,
        has_special_chars=True,
    )

    assert result == expected_password
