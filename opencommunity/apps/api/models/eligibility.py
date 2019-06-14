from .base import BaseModel
from .service import Service
from django.db import models

class Eligibility(BaseModel):
    eligibility = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
