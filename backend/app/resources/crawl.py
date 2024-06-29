from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db

blp = Blueprint("crawl", __name__, description="Operations on scrapy spider")
