from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.schemas import JobSchema

# The Blueprint is used to divide an api into multiple segments.

blp = Blueprint("jobs", __name__, description="Operations on jobs")

@blp.route("/job/<string:job_id>")
class Job(MethodView):
    @blp.response(200, JobSchema)
    def get(self, job_id):
        try:
            return jobs[job_id]
        except KeyError:
            abort(404, message="Job not found.")

@blp.route("/job")
class JobList(MethodView):
    @blp.response(200, JobSchema(many=True))
    def get(self):
        return jobs.values()