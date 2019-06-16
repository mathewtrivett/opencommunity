from rest_marshmallow import Schema, fields
from .base import BasicDetailsSchema
from .services import ServiceSchema
from .contacts import ContactSchema


class OrganisationSchema(BasicDetailsSchema):
    email = fields.Email()
    url = fields.Url()
    funding = fields.Nested(FundingSchema, many=True) # Probably want this to be a national data service of funders?
    contacts = fields.Nested(ContactSchema, many=True)
    locations = fields.Nested(LocationSchema, many=True)
    programs = fields.Nested(ProgramSchema, many=True)
    services = fields.Nested(ServiceSchema, many=True)
