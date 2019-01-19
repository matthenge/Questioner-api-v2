from flask import Blueprint
from flask_restful import Api, Resource

version2 = Blueprint('v2', __name__, url_prefix='/api/v2')

api = Api(version2, catch_all_404s=True)
