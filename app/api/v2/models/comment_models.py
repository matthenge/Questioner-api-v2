"""Module for comments operations"""
import json
from .base_models import BaseModels


class CommentModels(BaseModels):
    """Class for comments CRUD operations"""

    def __init__(self, userId, question, comment):
        """Initialize the comment models"""
        self.userId = userId
        self.question = question
        self.comment = comment

    def create_comment(self):
        """method for posting comments"""
        commnt = dict(
            userId=self.userId,
            question=self.question,
            comment=self.comment
        )
        commentData = {
            "comment": "comment"
        }
        table = "comments"
        columns = ", ".join(commnt.keys())
        values = "', '".join(map(str, commnt.values()))
        details = ",".join(map(str, commentData.values()))
        newComment = BaseModels.save_data(self, table, columns, values,
                                          details)
        newComment = json.dumps(newComment, default=str)

        return newComment

    def fetch_quest(self, questionId):
        """Method to fetch question"""
        data = "questionId, title, body"
        table = "questions"
        column = "questionId"
        search_item = questionId
        question = BaseModels.fetch_specific(self, data, table, column,
                                             search_item)
        question = json.dumps(question, default=str)
        return question

    def retrieve_all_by_one(self, questionId):
        """Method to fetch comments of a question"""
        table = "comments"
        columns = "userId, question, comment"
        column = "question"
        search_item = questionId
        comments = BaseModels.fetch_all_by_one(self, columns, table, column,
                                               search_item)
        comments = json.dumps(comments, default=str)
        return comments
