from rest_marshmallow import Schema, fields

class PhoneSchema(Schema):
    number = fields.String()
    type = fields.String()
    extension = fields.String()
    description = fields.String()

class ContactSchema(Schema):
    id = fields.UUID()
    name = fields.String()
    title = fields.String()
    email = fields.Email()
    phones = fields.Nested(PhoneSchema, many=True)
