from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from sqlalchemy import func

from db import db
from schemas.schemas import JobSchema
from models import JobModel, OrganizationModel

# The Blueprint is used to divide an api into multiple segments.

blp = Blueprint("jobs", __name__, description="Operations on jobs")

@blp.route("/job/<string:job_id>")
class Job(MethodView):
    @blp.response(200, JobSchema)
    def get(self, job_id):
        try:
            return JobModel.query.get_or_404(job_id)
        except KeyError:
            abort(404, message="Job not found.")

    def delete(self, job_id):
        job = JobModel.query.get_or_404(job_id)
        raise NotImplementedError("Job deletion is not yet implemented.")

@blp.route("/job")
class JobList(MethodView):
    @blp.response(200, JobSchema(many=True))
    def get(self):
        return JobModel.query.all()
    
    @blp.arguments(JobSchema)
    @blp.response(201, JobSchema)
    def put(self, job_data):
        organization_name = job_data.pop("organization_name")
        organization = OrganizationModel.query.filter_by(name=organization_name).first()

        if not organization:
            organization = OrganizationModel(name=organization_name)
            db.session.add(organization)
            try:
                db.session.commit()
            except:
                abort(500, message="An error occurred while inserting job.")


        job = JobModel(**job_data, organization_id=organization.id)

        try:
            db.session.add(job)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting job.")

        return job
    
@blp.route("/job/count")
class OrganizationCount(MethodView):
    def get(self):
        count = db.session.query(func.count(JobModel.id)).scalar()
        return {"count": count}