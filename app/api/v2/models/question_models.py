"""Module for question operations"""
import json
from .base_models import BaseModels


class QuestionModels(BaseModels):
    """Class for questions CRUD operations"""

    def __init__(self, createdBy, meetup, title, body):
        """Initialize the question models"""
        self.createdBy = createdBy
        self.meetup = meetup
        self.title = title
        self.body = body

    def create_question(self):
        """method for creating questions"""
        question = dict(
            createdBy=self.createdBy,
            meetup=self.meetup,
            title=self.title,
            body=self.body
        )
        questData = {
            "createdBy": "createdBy",
            "meetup": "meetup",
            "title": "title",
            "body": "body"
        }
        table = "questions"
        columns = ", ".join(question.keys())
        values = "', '".join(map(str, question.values()))
        details = ",".join(map(str, questData.values()))
        newQuest = BaseModels.save_data(self, table, columns, values, details)
        newQuest = json.dumps(newQuest, default=str)

        return newQuest

    def upvote(self, questionId, userId):
        """Method to upvote a question"""
        table = "questions"
        tbl = "voters"
        fields = "questionId, voterId"
        columns = "votes=votes+1"
        data = "meetup, title, body, votes"
        column = "questionId"
        search_item = questionId
        values = questionId, userId
        question = BaseModels.fetch_specific(self, data, table, column,
                                             search_item)
        question = json.dumps(question, default=str)
        question = json.loads(question)
        if not question:
            return "no question"
        user = BaseModels.fetch_some_data(self, fields, tbl, "voterId", userId,
                                          "questionId", questionId)
        user = json.dumps(user, default=str)
        user = json.loads(user)
        if user:
            return "voted"
        updated = BaseModels.update_record(self, table, columns, column,
                                           search_item)
        voter = BaseModels.insert_data(self, tbl, fields, questionId, userId)
        quiz = BaseModels.fetch_specific(self, data, table, column,
                                         search_item)
        quiz = json.dumps(quiz, default=str)
        quiz = json.loads(quiz)
        return quiz
