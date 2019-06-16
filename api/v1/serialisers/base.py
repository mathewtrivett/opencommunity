from rest_marshmallow import Schema, fields

class BasicDetailsSchema(Schema):
    id = fields.UUID(required=True)
    name = fields.String()
    alternate_name = fields.String()
    description = fields.String()
