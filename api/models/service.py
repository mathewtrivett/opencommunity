from .base import BaseModel, BasicDetails
from django.db import models
from .location import Location
from .taxonomy import Taxonomy
from .organisation import Organisation
from .eligibility import Eligibility

class Service(BasicDetails):

    ACTIVE = 'active'
    INACTIVE = 'inactive'
    TEMP_CLOSED = 'temporarily_closed'
    DEFUNCT = 'defunct'

    STATUSES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (TEMP_CLOSED, 'Temporarily Closed'),
        (DEFUNCT, 'Defunct')
    )

    email = models.EmailField()
    url = models.URLField()
    description = models.TextField(blank=True)
    wait_time = models.CharField(max_length=255)
    locations = models.ManyToManyField(Location, related_name='services')
    taxonomy = models.ManyToManyField(Taxonomy, related_name='services')
    status = models.CharField(max_length=60, choices=STATUSES,default=ACTIVE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    eligibility = models.OneToOneField(Eligibility, on_delete=models.CASCADE, null=True, related_name='service')
