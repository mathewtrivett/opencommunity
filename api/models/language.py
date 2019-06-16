from django.db import models

class Language(models.Model):
    iso_639_2 = models.CharField(max_length=10)
    iso_639_1 = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
