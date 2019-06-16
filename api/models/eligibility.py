from .base import BaseModel
from django.db import models
from django.core.validators import MinValueValidator

class Eligibility(BaseModel):
    """
    Eligibility
    ~~~~~~~~~~~~~~~~~~
    Implements an object to capture the eligibility criteria of a service.
    This includes the age range the service is for.
    """
    eligibility = models.TextField()
    min_age = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    max_age = models.IntegerField(null=True)
