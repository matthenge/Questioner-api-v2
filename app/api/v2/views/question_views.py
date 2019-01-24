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
                                 help="meetup field is missing")
        self.parser.add_argument("title", type=str,
                                 help="title field is missing")
        self.parser.add_argument("body", type=str, required=True,
                                 help="question body is missing")

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
                "error": "Meetup {} does not exist".format(meetup)
            }, 404
        if validate.valid_title(title):
            return validate.valid_title(title)
        if validate.valid_body(body):
            return validate.valid_body(body)
        question = QuestionModels(createdBy, meetup, title, body)
        newQuestion = question.create_question()
        newQuestion = json.loads(newQuestion)

        return {
            "status": 201,
            "data": [newQuestion]
        }, 201

    @login_required
    def get(self, current_user):
        """Fetch all questions"""
        questions = QuestionModels.get_all_questions(self)
        questions = json.loads(questions)
        if not questions:
            return {
                "status": 404,
                "error": "No questions posted yet"
            }, 404
        return {
            "status": 200,
            "data": questions
        }, 200


class Upvote(Resource):
    """Upvote question operation"""

    @login_required
    def patch(self, questionId, current_user):
        """Upvote question method"""
        userId = current_user["userid"]
        question = QuestionModels.upvote(self, questionId, userId)
        if question is False:
            return {
                "status": 404,
                "error": "Question {} does not exist".format(questionId)
            }, 404
        elif question is True:
            return {
                "status": 409,
                "error": "User {} has already voted".format(userId)
            }, 409
        return {
            "status": 200,
            "question": [question]
        }, 200


class Downvote(Resource):
    """Downvote question operation"""

    @login_required
    def patch(self, questionId, current_user):
        """Downvote question method"""
        userId = current_user["userid"]
        question = QuestionModels.downvote(self, questionId, userId)
        if question is False:
            return {
                "status": 404,
                "error": "Question {} does not exist".format(questionId)
            }, 404
        elif question is True:
            return {
                "status": 409,
                "error": "User {} already voted".format(userId)
            }, 409
        return {
            "status": 200,
            "question": [question]
        }, 200
