from db import db

class JobModel(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    date_posted = db.Column(db.Date(), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.id"), unique=False, nullable=False)
    organization = db.relationship("OrganizationModel", back_populates="jobs")