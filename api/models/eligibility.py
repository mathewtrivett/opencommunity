from .base import BaseModel
from django.db import models
from django.core.validators import MinValueValidator

class Eligibility(BaseModel):
    eligibility = models.TextField()
    min_age = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    max_age = models.IntegerField(null=True)
