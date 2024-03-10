from typing import Awaitable, Callable

from fastapi import FastAPI
from tortoise import Tortoise

from app.db import TORTOISE_ORM


async def _setup_db(app: FastAPI) -> None:  # pragma: no cover
    await Tortoise.init(TORTOISE_ORM)


def register_startup_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application startup.

    This function uses fastAPI app to store data
    inthe state, such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event('startup')
    async def _startup() -> None:  # noqa: WPS430
        await _setup_db(app)

    return _startup


def register_shutdown_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application's shutdown.

    :param app: fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event('shutdown')
    async def _shutdown() -> None:  # noqa: WPS430
        await Tortoise.close_connections()

    return _shutdown
