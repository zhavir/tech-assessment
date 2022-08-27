import random
from typing import List


class RandomizerProvider:

    @classmethod
    async def randomize(
        cls,
        *,
        values: List[str],
        length: int,
    ) -> List[str]:
        return [random.choice(values) for _ in range(length)]
