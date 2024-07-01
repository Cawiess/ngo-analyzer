from marshmallow import Schema, fields, validate

class BaseJobSchema(Schema):
    id = fields.Str(dump_only=True)
    job_title = fields.Str(required=True)
    grade = fields.Str(required=True)
    occupational_groups = fields.List(fields.String(validate=validate.Length(min=1)), required=True)
    location = fields.Str(required=True)
    organization_name = fields.Str(required=True)
    closing_date = fields.Date(required=True)
    job_description = fields.Str(required=True)

class BaseOrganizationSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class OrganizationSchema(BaseOrganizationSchema):
    jobs = fields.List(fields.Nested(BaseJobSchema(), dump_only=True))

class JobSchema(BaseJobSchema):
    #organization_id = fields.Int(required=True, load_only=True)
    organization = fields.Pluck(BaseOrganizationSchema(), 'name', dump_only=True)