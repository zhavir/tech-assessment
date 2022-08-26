from typing import Generator
from unittest.mock import AsyncMock

import pytest
from httpx import AsyncClient
from pytest_mock import MockerFixture

from app.main import app, SERVICE_NAME


@pytest.fixture(scope="function")
def mocked_client() -> Generator[AsyncClient, None, None]:
    yield AsyncClient(app=app, base_url=f'http://{SERVICE_NAME}:9001')


@pytest.fixture(scope="function")
def mocked_password_generator_service(mocker: MockerFixture) -> Generator[AsyncMock, None, None]:
    yield mocker.patch(
        'app.routers.password_generation_router.PasswordGeneratorService',
    )

