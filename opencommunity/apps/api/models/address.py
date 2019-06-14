from .base import BaseModel
from .location import Location
from django.db import models

class BaseAddress(BaseModel):
    street_address = models.CharField(max_length=255,blank=False)
    city = models.CharField(max_length=255, blank=False)
    region = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=255, blank=False)
    uprn = models.CharField(max_length=255)

class PostalAddress(BaseAddress):
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

class PhysicalAddress(BaseAddress):
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
