from pydantic import BaseModel, conint, root_validator

from app.settings import settings


class GeneratePasswordRequest(BaseModel):
    password_length: conint(gt=0, le=200) = settings.default_password_length  # type: ignore
    has_numbers: bool = settings.default_has_numbers
    has_lowercase_chars: bool = settings.default_has_lowercase_chars
    has_uppercase_chars: bool = settings.default_has_uppercase_chars
    has_special_chars: bool = settings.default_has_special_chars

    @root_validator
    def check_all_flags_are_not_disabled(cls, values: dict) -> dict:
        if not any(
            (
                values.get('has_numbers'),
                values.get('has_lowercase_chars'),
                values.get('has_uppercase_chars'),
                values.get('has_special_chars'),
            )
        ):
            raise ValueError('At least one flag must be enabled')
        return values
