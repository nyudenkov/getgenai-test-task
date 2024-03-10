from typing import Optional

from fastapi import APIRouter, status, Depends
from pydantic import UUID4

from app.web.api.dependencies import get_api_key
from app.web.api.documents import schema, service

router = APIRouter()


@router.post(
    '',
    response_model=schema.DocumentModel,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_api_key)],
)
async def create_document(data: schema.DocumentCreateModel) -> schema.DocumentModel:
    return await service.create_document(data)


@router.put(
    '/{document_id}',
    response_model=schema.DocumentModel,
    dependencies=[Depends(get_api_key)],
)
async def update_document(
        document_id: UUID4,
        data: schema.DocumentUpdateModel,
) -> schema.DocumentModel:
    return await service.update_document(document_id, data)


@router.delete(
    '/{document_id}',
    dependencies=[Depends(get_api_key)],
)
async def delete_document(document_id: UUID4) -> None:
    await service.delete_document(document_id)


@router.get(
    '/{document_id}',
    response_model=schema.DocumentModel,
    dependencies=[Depends(get_api_key)],
)
async def get_document(document_id: UUID4) -> schema.DocumentModel:
    return await service.get_document(document_id)


# TODO: Make pagination (!)
@router.get(
    '',
    response_model=list[schema.DocumentModel],
    dependencies=[Depends(get_api_key)]
)
async def get_documents() -> list[schema.DocumentModel]:
    return await service.get_documents()
