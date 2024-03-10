import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status

from app.web.api.documents import schema

document_create_data = schema.DocumentCreateModel(
    title="Test Document",
    content="Some content",
    status="draft",
)


@pytest.mark.anyio
async def test_create_document(client_with_auth: AsyncClient, app: FastAPI) -> None:
    response = await client_with_auth.post("/api/documents", json=document_create_data.dict())
    print(response.request.url)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.anyio
async def test_get_documents(client_with_auth: AsyncClient, app: FastAPI) -> None:
    response = await client_with_auth.get("/api/documents")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)
