import uuid

from tortoise import models, fields

__all__ = ['Document']


class Document(models.Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    title = fields.CharField(max_length=256)
    content = fields.TextField()
    status = fields.CharField(max_length=16)  # idk what this field should do ¯\_(ツ)_/¯ so, imagination

    class Meta:
        table = "documents"
