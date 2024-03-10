from pydantic import BaseModel, UUID4


class DocumentBaseModel(BaseModel):
    title: str
    content: str
    status: str


class DocumentCreateModel(DocumentBaseModel):
    pass


class DocumentUpdateModel(DocumentBaseModel):
    pass


class DocumentModel(DocumentBaseModel):
    id: UUID4

    class Config:
        from_attributes = True
