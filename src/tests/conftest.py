from typing import Generator

import pytest
from httpx import AsyncClient

from app.main import app, SERVICE_NAME


@pytest.fixture(scope="function")
def mocked_client() -> Generator[AsyncClient, None, None]:
    yield AsyncClient(app=app, base_url=f'http://{SERVICE_NAME}:9001')
