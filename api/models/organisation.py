from .base import BaseModel, BasicDetails
from django.db import models

class Organisation(BasicDetails):
    email = models.EmailField()
    url = models.URLField()
