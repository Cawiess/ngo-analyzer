# Starts the Flask application making it ready to accept requests

from flask import Flask
from flask_smorest import Api

from app.resources.job import blp as JobBlueprint
from app.resources.organization import blp as OrganizationBlueprint

app = Flask(__name__)


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Jobs REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(JobBlueprint)
api.register_blueprint(OrganizationBlueprint)