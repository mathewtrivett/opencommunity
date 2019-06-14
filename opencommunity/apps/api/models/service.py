from .base import BaseModel, BasicDetails
from django.db import models
from .location import Location
from .taxonomy import Taxonomy

class Service(BasicDetails):
    email = models.EmailField()
    url = models.URLField()
    description = models.TextField(blank=True)
    wait_time = models.CharField(max_length=255)
    locations = models.ManyToManyField(Location, related_name='services')
    taxonomy = models.ManyToManyField(Taxonomy)
