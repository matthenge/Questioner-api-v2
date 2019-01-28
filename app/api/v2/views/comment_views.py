"""Module for comment views"""
from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from app.api.v2.models.comment_models import CommentModels
from flask_restful.reqparse import RequestParser
from app.api.v2.utils.validator import Validators
from app.api.v2.utils.authentication import login_required
import json

validate = Validators()


class AllComments(Resource):
    """Class for comments endpoints"""
    def __init__(self):
        """Initialize the comments class"""
        self.parser = RequestParser()
        self.parser.add_argument("question", type=int, required=True,
                                 help="please input a valid questionId")
        self.parser.add_argument("comment", type=str,
                                 help="please input a valid comment")

    @login_required
    def post(self, current_user):
        """Create comment endpoint"""
        userId = current_user["userid"]
        args = self.parser.parse_args()
        args = request.get_json()
        question = args["question"]
        comment = args["comment"]

        question_exists = CommentModels.fetch_quest(self, question)
        question_exists = json.loads(question_exists)
        if not question_exists:
            return {
                "status": 404,
                "error": "Question {} does not exist".format(question)
            }, 404
        if validate.valid_strings(comment):
            return validate.valid_strings(comment)
        cmmnt = CommentModels(userId, question, comment)
        newComment = cmmnt.create_comment()
        newComment = json.loads(newComment)

        return {
            "status": 201,
            "data": [
                question_exists,
                newComment
            ]
        }, 201

    @login_required
    def get(self, current_user):
        """Fetch all comments by user"""
        userId = current_user["userid"]
        comments = CommentModels.retrieve_all_by_user(self, userId)
        comments = json.loads(comments)
        if not comments:
            return {
                "status": 404,
                "error": "No comments posted by user {}\
                ".format(userId)
            }, 404
        return {
            "status": 200,
            "data": comments
        }, 200


class QuestionComments(Resource):
    """Question comments"""

    @login_required
    def get(self, questionId, current_user):
        """Fetch all comments of one question"""
        comments = CommentModels.retrieve_all_by_one(self, questionId)
        comments = json.loads(comments)
        if not comments:
            return {
                "status": 404,
                "error": "No comments posted for question {}\
                ".format(questionId)
            }, 404
        return {
            "status": 200,
            "data": comments
        }, 200
