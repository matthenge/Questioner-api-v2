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
                                 help="location field is missing")
        self.parser.add_argument("images", type=str, required=True,
                                 help="Image field is missing")
        self.parser.add_argument("topic", type=str, required=True,
                                 help="Topic field is missing")
        self.parser.add_argument("happeningOn", type=str, required=True,
                                 help="Date field is missing")
        self.parser.add_argument("tags", type=str, required=True,
                                 help="Tags field seems to be missing")

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

        if validate.valid_date(happeningOn):
            return validate.valid_date(happeningOn)
        if validate.valid_topic(topic):
            return validate.valid_topic(topic)
        if validate.valid_location(location):
            return validate.valid_location(location)
        if validate.valid_time(happeningOn):
            return validate.valid_time(happeningOn)
        meetup = MeetupModels(userId, location, images, topic, happeningOn,
                              tags)
        newMeetup = meetup.create_meetup()
        newMeetup = json.loads(newMeetup)

        return {
            "status": 201,
            "meetup": newMeetup
        }, 201

    @login_required
    def get(self, current_user):
        """Fetch all meetups"""
        meetups = MeetupModels.get_all(self)
        meetups = json.loads(meetups)
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
        meetups = json.loads(meetups)
        if not meetups:
            return {
                "status": 404,
                "error": "No Upcoming Meetups"
            }, 404
        return {
                "status": 200,
                "meetups": meetups
            }, 200


class OneMeetup(Resource):
    """Class for specific meetup"""

    @login_required
    def get(self, meetupId, current_user):
        """Method to fetch specific meetup"""
        meetup = MeetupModels.get_specific(self, meetupId)
        meetup = json.loads(meetup)
        if not meetup:
            return {
                "status": 404,
                "error": "Meetup {} does not exist".format(meetupId)
            }, 404
        return {
                "status": 200,
                "meetups": meetup
            }, 200

    @admin_required
    def delete(self, meetupId, current_user):
        """Method to delete meetup record"""
        delete_meetup = MeetupModels.delete_specific(self, meetupId)
        if delete_meetup is False:
            return {
                "status": 404,
                "error": "Meetup {} does not exist".format(meetupId)
            }, 404
        return {
                "status": 200,
                "data": "Meetup {} deleted".format(meetupId)
            }, 200
