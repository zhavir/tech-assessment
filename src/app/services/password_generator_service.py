from app.providers.randomizer_provider import RandomizerProvider
from app.utils.get_string_chars import get_string_chars


class PasswordGeneratorService:

    def __init__(self, *, randomizer_service: RandomizerProvider):
        self.randomizer_service = randomizer_service

    async def generate_password(
        self,
        *,
        password_length: int,
        has_numbers: bool,
        has_lowercase_chars: bool,
        has_uppercase_chars: bool,
        has_special_chars: bool,
    ) -> str:
        allowed_chars = await get_string_chars(
            numbers=has_numbers,
            lowercase_letters=has_lowercase_chars,
            uppercase_letters=has_uppercase_chars,
            special_chars=has_special_chars,
        )
        random_sample = await self.randomizer_service.randomize(values=allowed_chars, length=password_length)
        return ''.join(random_sample)
