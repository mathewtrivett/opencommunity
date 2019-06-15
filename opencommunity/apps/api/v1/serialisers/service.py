from rest_marshmallow import Schema, fields
from .base import BasicDetailsSchema
from .contact import ContactSchema
from .eligibility import EligibilitySchema
from .language import LanguageSchema

class ServiceSchema(BasicDetailsSchema):
    email = fields.Email()
    url = fields.Url()
    status = fields.String()
    contacts = fields.Nested(ContactSchema, many=True)
    eligibility = fields.Nested(EligibilitySchema, many=True)
    languages = fields.Nested(LanguageSchema, many=True)
