"""Module for question views"""
from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from app.api.v2.models.question_models import QuestionModels
from app.api.v2.models.meetup_models import MeetupModels
from flask_restful.reqparse import RequestParser
from app.api.v2.utils.validator import Validators
from app.api.v2.utils.authentication import login_required
import json

validate = Validators()


class AllQuestions(Resource):
    """Class for questions endpoints"""
    def __init__(self):
        """Initialize the questions class"""
        self.parser = RequestParser()
        self.parser.add_argument("meetup", type=int, required=True,
                                 help="please input a valid meetupId")
        self.parser.add_argument("title", type=str,
                                 help="please input a valid title")
        self.parser.add_argument("body", type=str, required=True,
                                 help="please input a valid body")

    @login_required
    def post(self, current_user):
        """Create question endpoint"""
        createdBy = current_user["userid"]
        args = self.parser.parse_args()
        args = request.get_json()
        meetup = args["meetup"]
        title = args["title"]
        body = args["body"]

        meetup_exists = MeetupModels.get_specific(self, meetup)
        meetup_exists = json.loads(meetup_exists)
        if not meetup_exists:
            return {
                "status": 404,
                "error": "Meetup does not exist"
            }, 404
        if validate.valid_strings(title, body):
            return validate.valid_strings(title, body)
        question = QuestionModels(createdBy, meetup, title, body)
        newQuestion = question.create_question()
        newQuestion = json.loads(newQuestion)

        return {
            "status": 201,
            "data": [newQuestion]
        }, 201
