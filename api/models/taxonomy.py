from .base import BaseModel
from django.db import models

class Taxonomy(BaseModel):
    name = models.CharField(max_length=255,blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    vocabulary = models.CharField( max_length=255, blank=True)

    class Meta:
        verbose_name_plural = 'Taxonomy'

    def __str__(self):
        return self.name
