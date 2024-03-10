from fastapi import HTTPException, status
from pydantic import UUID4

from app.db.models import Document
from app.web.api.documents import schema


async def create_document(data: schema.DocumentCreateModel) -> schema.DocumentModel:
    document = await Document.create(**data.dict())
    return schema.DocumentModel.from_orm(document)


async def update_document(document_id: UUID4, data: schema.DocumentUpdateModel) -> schema.DocumentModel:
    document = await Document.get_or_none(id=document_id)
    if not document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Document not found')
    await document.update_from_dict(**data.dict())
    await document.save()
    return schema.DocumentModel.from_orm(document)


async def delete_document(document_id: UUID4) -> None:
    await Document.filter(id=document_id).delete()


async def get_document(document_id: UUID4) -> schema.DocumentModel:
    document = await Document.get_or_none(id=document_id)
    if not document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Document not found')
    return schema.DocumentModel.from_orm(document)


async def get_documents() -> list[schema.DocumentModel]:
    documents = await Document.all()
    return [schema.DocumentModel.from_orm(document) for document in documents]
