from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from app.api.v2.models.meetup_models import MeetupModels
from app.api.v2.models.user_models import UserModels
from flask_restful.reqparse import RequestParser
from datetime import datetime
from app.api.v2.utils.validator import Validators
from app.api.v2.utils.authentication import login_required, admin_required
import json

validate = Validators()


class AllMeetups(Resource):
    """Class for meetup endpoints"""
    def __init__(self):
        """Initialize the meetup class"""
        self.parser = RequestParser()
        self.parser.add_argument("location", type=str, required=True,
                                 help="please input a valid location")
        self.parser.add_argument("images", type=str,
                                 help="please input a valid image url")
        self.parser.add_argument("topic", type=str, required=True,
                                 help="please input a valid topic")
        self.parser.add_argument("happeningOn",
                                 type=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M"),
                                 required=True, help="Format yyyy-mm-dd hh:mm")
        self.parser.add_argument("tags", type=str,
                                 help="please input a valid tags")

    @admin_required
    def post(self, current_user):
        """Create meetup endpoint"""
        userId = current_user["userid"]
        args = self.parser.parse_args()
        args = request.get_json()
        location = args["location"]
        images = args["images"]
        topic = args["topic"]
        happeningOn = args["happeningOn"]
        tags = args["tags"]

        if validate.valid_strings(location, topic):
            return validate.valid_strings(location, topic)
        if validate.valid_time(happeningOn):
            return validate.valid_time(happeningOn)
        meetup = MeetupModels(userId, location, images, topic, happeningOn,
                              tags)
        meetup.create_meetup()

        return {
            "message": "Meetup Created Successfully",
            "meetup": meetup.__dict__
        }, 201

    @login_required
    def get(self, current_user):
        """Fetch all meetups"""
        meetups = MeetupModels.get_all(self)
        if not meetups:
            return {
                "status": 404,
                "error": "No meetups posted yet"
            }, 404
        return {
            "status": 200,
            "data": meetups
        }, 200


class Upcoming(Resource):
    """Class for Upcoming meetups"""

    @login_required
    def get(self, current_user):
        """Method to fetch only upcoming meetups"""
        meetups = MeetupModels.get_upcoming(self)
        if not meetups:
            return {
                "error": "No Upcoming Meetups",
                "status": 404
            }, 404
        return {
                "status": 200,
                "meetups": meetups
            }, 200
