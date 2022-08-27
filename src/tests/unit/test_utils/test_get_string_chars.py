import string
from typing import List

import pytest

from app.utils.get_string_chars import get_string_chars


@pytest.mark.parametrize(
    ['numbers', 'lowercase_letters', 'uppercase_letters', 'special_chars', 'expected'],
    [
        (True, False, False, False, list(string.digits)),
        (False, True, False, False, list(string.ascii_lowercase)),
        (False, False, True, False, list(string.ascii_uppercase)),
        (False, False, False, True, list(string.punctuation)),
        (
            True, True, True, True, list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase) +
            list(string.punctuation)
        ),
        (False, False, False, False, []),
    ],
)
@pytest.mark.asyncio
async def test_get_string_chars(
    numbers: bool,
    lowercase_letters: bool,
    uppercase_letters: bool,
    special_chars: bool,
    expected: List[str],
):
    result = await get_string_chars(
        numbers=numbers,
        lowercase_letters=lowercase_letters,
        uppercase_letters=uppercase_letters,
        special_chars=special_chars,
    )

    assert result == expected
