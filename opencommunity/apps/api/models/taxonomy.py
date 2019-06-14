from .base import BaseModel
from django.db import models

class Taxonomy(BaseModel):
    name = models.CharField(max_length=255,blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,blank=True)
    vocabulary = models.CharField( max_length=255, blank=True)
