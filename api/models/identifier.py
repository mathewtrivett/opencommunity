from django.db import models
from .base import BaseModel
from .organisation import Organisation
from .identification_body import IdentificationBody

class Identifier(BaseModel):
    """
    Identifier
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    An identifier is a unique registration that organisations have with identifiers.
    """
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=255, null=False, unique=True)
    identification_body = models.ForeignKey(IdentificationBody, on_delete=models.CASCADE)
