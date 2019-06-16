from .base import BaseModel
from .service import Service
from django.db import models


class Document(BaseModel):
    name = models.CharField(max_length=255)

class RequiredDocument(BaseModel):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    detail = models.TextField()
