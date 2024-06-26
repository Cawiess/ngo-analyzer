# Starts the Flask application making it ready to accept requests
import os

from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from dotenv import load_dotenv

from db import db
import models

from resources.job import blp as JobBlueprint
from resources.organization import blp as OrganizationBlueprint

# Factory pattern
def create_app(db_url=None): 
    app = Flask(__name__)
    load_dotenv()


    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Jobs REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate = Migrate(app, db)
    #with app.app_context():
    #    db.create_all()

    api = Api(app)
    api.register_blueprint(JobBlueprint)
    api.register_blueprint(OrganizationBlueprint)

    return app