import string
from typing import List

import pytest

from app.providers.randomizer_provider import RandomizerProvider


@pytest.mark.parametrize(
    ["values", "length"],
    [
        (["test"], 1),
        (["test"], 0),
        (["test", "test2"], 1),
        (list(string.digits), 5),
    ]
)
@pytest.mark.asyncio
async def test_generate_random_sample(values: List[str], length: int):
    service = RandomizerProvider()

    result = await service.randomize(values=values, length=length)

    assert result is not None
    assert len(result) == length
