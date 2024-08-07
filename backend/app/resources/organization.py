import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func

from db import db
from models import OrganizationModel
from schemas.schemas import OrganizationSchema

# The Blueprint is used to divide an api into multiple segments.

blp = Blueprint("organizations", __name__, description="Operations on organizations")

@blp.route("/organization/id/<string:organization_id>")
class Organization(MethodView):
    @blp.response(200, OrganizationSchema)
    def get(self, organization_id):
        organization = OrganizationModel.query.get_or_404(organization_id)
        return organization
    
@blp.route("/organization/name/<string:name>")
class OrganizationByName(MethodView):
    @blp.response(200, OrganizationSchema)
    def get(self, name):
        organization = OrganizationModel.query.filter_by(name=name).first()
        if not organization:
            abort(404, message="Organization not found.")
        return organization


@blp.route("/organization")
class OrganizationList(MethodView):
    @blp.response(200, OrganizationSchema(many=True))
    def get(self):
        return OrganizationModel.query.all()
    
    @blp.arguments(OrganizationSchema)
    @blp.response(201, OrganizationSchema)
    def put(self, organization_data):
        organization = OrganizationModel(**organization_data)

        try:
            db.session.add(organization)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting organization.")

        return organization
    
@blp.route("/organization/count")
class OrganizationCount(MethodView):
    def get(self):
        count = db.session.query(func.count(OrganizationModel.id)).scalar()
        return {"count": count}