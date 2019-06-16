from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BasicDetails(BaseModel):
    name = models.CharField(blank=False, max_length=255)
    alternate_name = models.CharField(max_length=255)
    description = models.TextField(blank=False)

    class Meta:
        abstract = True
