from db import db

class JobModel(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(80), nullable=False)
    grade = db.Column(db.String(80), nullable=False)
    occupational_groups = db.Column(db.ARRAY(db.String), nullable=False)
    job_description = db.Column(db.Text(), nullable=False)
    closing_date = db.Column(db.Date(), nullable=False)
    location = db.Column(db.String(80), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.id"), unique=False, nullable=False)
    organization = db.relationship("OrganizationModel", back_populates="jobs")

