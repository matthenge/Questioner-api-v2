"""Module for rsvp views"""
from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from app.api.v2.models.rsvp_models import RsvpModels
from app.api.v2.models.meetup_models import MeetupModels
from flask_restful.reqparse import RequestParser
from app.api.v2.utils.validator import Validators
from app.api.v2.utils.authentication import login_required
import json

validate = Validators()


class Rsvps(Resource):
    """Class for Rsvps endpoints"""
    def __init__(self):
        """Initialize the rsvps class"""
        self.parser = RequestParser()
        self.parser.add_argument("response", type=str, required=True,
                                 help="Input a 'yes', 'no' or 'maybe'")

    @login_required
    def post(self, meetupId, current_user):
        """Create rsvp endpoint"""
        createdBy = current_user["userid"]
        args = self.parser.parse_args()
        args = request.get_json()
        response = args["response"]
        meetup = meetupId
        meetup_exists = MeetupModels.get_one(self, meetup)
        meetup_exists = json.loads(meetup_exists)
        if not meetup_exists:
            return {
                "status": 404,
                "error": "Meetup does not exist"
            }, 404
        user = RsvpModels.check_user(self, createdBy, meetup)
        if user:
            return {
                "status": 403,
                "error": "User already reserved a spot"
            }, 403
        if validate.valid_response(response):
            return validate.valid_response(response)
        rsvp = RsvpModels(meetup, createdBy, response)
        newRsvp = rsvp.create_rsvp()
        newRsvp = json.loads(newRsvp)

        return {
            "status": 201,
            "data": [
                meetup_exists,
                newRsvp
            ]
        }, 201
