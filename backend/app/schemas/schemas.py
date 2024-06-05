from marshmallow import Schema, fields

class JobSchema(Schema):
    id = fields.Str(dump_only=True)
    organization_id = fields.Str(required=True)
    country = fields.Str(required=True)
    title = fields.Str(required=True)
    date_posted = fields.Str(required=True)
    description = fields.Str(required=True)

class OrganizationSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)