from .base import BaseModel
from django.db import models
from .language import Language

"""
Contact should comply with the vCard format allowing for contacts
to be saved to common address book applications.
"""

class Contact(BaseModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    email = models.EmailField()

class Phone(BaseModel):
    TEXT = 'text'
    VOICE = 'voice'
    FAX = 'fax'
    CELL = 'cell'
    VIDEO = 'video'
    PAGER = 'pager'
    TEXTPHONE = 'textphone'

    PHONE_TYPES = [
        (TEXT,'Text (SMS)'),
        (VOICE,'Voice'),
        (FAX,'Fax'),
        (CELL, 'Mobile'),
        (VIDEO, 'Video conferencing'),
        (PAGER,'Pager'),
        (TEXTPHONE,'Textphone')
    ]

    number = models.CharField(blank=False, max_length=80)
    extension = models.IntegerField()
    type = models.CharField(choices = PHONE_TYPES, default=VOICE, max_length=60)
    description = models.CharField(max_length=400)
    languages = models.ManyToManyField(Language)
