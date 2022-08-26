import pytest
from pydantic import ValidationError

from app.routers.models.requests import GeneratePasswordRequest
from app.settings import settings


@pytest.mark.parametrize(
    [
        'password_length',
        'has_numbers',
        'has_lowercase_chars',
        'has_uppercase_chars',
        'has_special_chars',
    ],
    [
        (100, True, True, True, True),
        (200, True, True, True, True),
        (1, False, False, False, True),
        (1, True, False, False, False),
        (
            settings.default_password_length,
            settings.default_has_numbers,
            settings.default_has_lowercase_chars,
            settings.default_has_uppercase_chars,
            settings.default_has_special_chars,
        ),
    ],
)
def test_validator_on_generate_password_request_model(
    password_length: int,
    has_numbers: bool,
    has_lowercase_chars: bool,
    has_uppercase_chars: bool,
    has_special_chars: bool,
):
    request = GeneratePasswordRequest(
        password_length=password_length,
        has_numbers=has_numbers,
        has_lowercase_chars=has_lowercase_chars,
        has_uppercase_chars=has_uppercase_chars,
        has_special_chars=has_special_chars,
    )
    assert request is not None


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
    ],
)
def test_validator_on_generate_password_request_model_raise_validation_error(
    password_length: int,
    has_numbers: bool,
    has_lowercase_chars: bool,
    has_uppercase_chars: bool,
    has_special_chars: bool,
):
    with pytest.raises(ValidationError):
        GeneratePasswordRequest(
            password_length=password_length,
            has_numbers=has_numbers,
            has_lowercase_chars=has_lowercase_chars,
            has_uppercase_chars=has_uppercase_chars,
            has_special_chars=has_special_chars,
        )
