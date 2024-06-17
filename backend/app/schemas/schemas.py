from marshmallow import Schema, fields

class BaseJobSchema(Schema):
    id = fields.Str(dump_only=True)
    country = fields.Str(required=True)
    title = fields.Str(required=True)
    date_posted = fields.Date(required=True)
    description = fields.Str(required=True)

class BaseOrganizationSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class OrganizationSchema(BaseOrganizationSchema):
    jobs = fields.List(fields.Nested(BaseJobSchema(), dump_only=True))

class JobSchema(BaseJobSchema):
    organization_id = fields.Int(required=True, load_only=True)
    organization = fields.Pluck(BaseOrganizationSchema(), 'name', dump_only=True)


