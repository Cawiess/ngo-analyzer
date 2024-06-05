from marshmallow import Schema, fields

class BaseJobSchema(Schema):
    id = fields.Str(dump_only=True)
    #organization_id = fields.Str(required=True)
    country = fields.Str(required=True)
    title = fields.Str(required=True)
    date_posted = fields.Str(required=True)
    description = fields.Str(required=True)

class BaseOrganizationSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class OrganizationSchema(BaseOrganizationSchema):
    jobs = fields.List(fields.Nested(BaseJobSchema(), dump_only=True))

class JobSchema(BaseJobSchema):
    organization_id = fields.Str(required=True, load_only=True)
    job = fields.Nested(BaseJobSchema(), dump_only=True)

