from .base import BaseModel, BasicDetails
from django.contrib.gis.db import models

class Location(BaseModel):
    name = models.CharField(max_length=255,blank=True)
    alternate_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    point = models.PointField()
    transportation = models.TextField()


class ServiceArea(BaseModel):
    description = models.TextField()
