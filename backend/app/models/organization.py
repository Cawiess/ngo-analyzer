from db import db

class OrganizationModel(db.Model):
    __tablename__ = "organizations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    jobs = db.relationship("JobModel", back_populates="organization", lazy="dynamic")