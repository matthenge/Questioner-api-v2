from flask import Blueprint
from flask_restful import Api, Resource
from app.api.v2.views.user_views import Users, UserLogin
from app.api.v2.views.meetup_views import AllMeetups

version2 = Blueprint('v2', __name__, url_prefix='/api/v2')

api = Api(version2, catch_all_404s=True)

api.add_resource(Users, '/auth/signup', strict_slashes=False)
api.add_resource(UserLogin, '/auth/login', strict_slashes=False)
api.add_resource(AllMeetups, '/meetups', strict_slashes=False)
