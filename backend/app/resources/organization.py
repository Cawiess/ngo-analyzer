import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.schemas import OrganizationSchema

# The Blueprint is used to divide an api into multiple segments.

blp = Blueprint("organizations", __name__, description="Operations on organizations")

@blp.route("/organization/<string:organization_id>")
class Organization(MethodView):
    @blp.response(200, OrganizationSchema)
    def get(self, organization_id):
        try:
            return organizations[organization_id]
        except KeyError:
            abort(404, message="Job not found.")

    def post(self, organization_id):
        pass

@blp.route("/organization")
class OrganizationList(MethodView):
    @blp.response(200, OrganizationSchema(many=True))
    def get(self):
        return organizations.values()

    def post(self):
        organization_data = request.get_json()
        organization_id = uuid.uuid4().hex
        organization = {**organization_data, "id": organization_id}
        organizations[organization_id] = organization

        return organization
