from .base import BaseModel, BasicDetails
from .address import PhysicalAddress
from django.db import models

class Organisation(BasicDetails):
    email = models.EmailField()
    url = models.URLField()
    physical_address = models.ForeignKey(PhysicalAddress,null=True,blank=True,on_delete=models.CASCADE)
