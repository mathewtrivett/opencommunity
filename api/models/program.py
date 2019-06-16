from .base import BaseModel
from .organisation import Organisation

class Program(BaseModel):
    name = models.CharField()
    alternate_name = models.CharField()
    organisation = models.ForeignKeyField(Organisation, on_delete = models.CASCADE)
