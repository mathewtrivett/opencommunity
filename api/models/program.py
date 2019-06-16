from .base import BaseModel
from .organisation import Organisation
from django.db import models

class Program(BaseModel):
    name = models.CharField(max_length=255)
    alternate_name = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation,on_delete = models.CASCADE)
