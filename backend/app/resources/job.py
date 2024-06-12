from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from schemas.schemas import JobSchema
from models import JobModel

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
        job = JobModel(**job_data)

        try:
            db.session.add(job)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting job.")

        return job