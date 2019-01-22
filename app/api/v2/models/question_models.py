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
