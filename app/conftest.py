from typing import Any, AsyncGenerator

import nest_asyncio
import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from tortoise import Tortoise
from tortoise.contrib.test import finalizer, initializer

from app.db import MODELS, TORTOISE_ORM
from app.settings import settings
from app.web.application import get_app

nest_asyncio.apply()


@pytest.fixture(scope='session')
def anyio_backend() -> str:
    """
    Backend for anyio pytest plugin.

    :return: backend name.
    """
    return 'asyncio'


@pytest.fixture(autouse=True)
async def initialize_db() -> AsyncGenerator[None, None]:
    """
    Initialize models and database.

    :yields: Nothing.
    """
    db_url = str(settings.db_url)

    initializer(
        MODELS,
        db_url=db_url,
        app_label='models',
    )

    await Tortoise.init(config=TORTOISE_ORM)

    yield

    await Tortoise.close_connections()
    finalizer()


@pytest.fixture
def app() -> FastAPI:
    """
    Fixture for creating FastAPI app.

    :return: fastapi app with mocked dependencies.
    """
    return get_app()


@pytest.fixture
async def client(
    app: FastAPI,
    anyio_backend: Any,
) -> AsyncGenerator[AsyncClient, None]:
    """
    Fixture that creates client for requesting server.

    :param fastapi_app: the application.
    :yield: client for the app.
    """
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac


@pytest.fixture
async def client_with_auth(client: AsyncClient, app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    access_token = settings.access_token

    async with AsyncClient(app=app, base_url='http://test', headers={'access_token': f'{access_token}'}) as ac:
        yield ac
