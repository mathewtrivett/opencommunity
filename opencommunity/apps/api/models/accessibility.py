from .base import BaseModel

class AccessibilityDetails(BaseModel):
    accessibility = models.CharField()
    details = models.TextField()
