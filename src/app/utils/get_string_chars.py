import string
from typing import List


async def get_string_chars(
    *,
    numbers: bool,
    lowercase_letters: bool,
    uppercase_letters: bool,
    special_chars: bool,
) -> List[str]:
    allowed_chars: List[str] = []

    if numbers:
        allowed_chars.extend(string.digits)

    if lowercase_letters:
        allowed_chars.extend(string.ascii_lowercase)

    if uppercase_letters:
        allowed_chars.extend(string.ascii_uppercase)

    if special_chars:
        allowed_chars.extend(string.punctuation)
    return allowed_chars
