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
                "error": "Question does not exist"
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
