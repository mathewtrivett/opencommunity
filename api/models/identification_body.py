from django.db import models
from .base import BaseModel

class IdentificationBody(BaseModel):
    """
    IdentificationBody is a body that holds registers of organisations.
    For example Companies House, Charities Commission, Ofsted etc.
    """
    name = models.CharField(max_length=128,unique=True)

    class Meta:
        verbose_name_plural = 'Identification bodies'

    def __str__(self):
        return self.name
