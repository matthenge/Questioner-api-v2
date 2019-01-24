from app import create_app
from .base_tests import BaseTest
import json


class TestComments(BaseTest):
    """Test Questions"""

    def test_post_question(self):
        """Test create question endpoint"""
        self.meetups()
        response = self.questions()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 201)
        self.assertIn("createdby", result.get("data")[0])

    def test_get_all_questions(self):
        """Test get all questions endpoint"""
        self.meetups()
        self.questions()
        response = self.get_all_questions()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("questionid", result.get("data")[0])

    def test_upvote_questions(self):
        """Test upvote questions endpoint"""
        self.meetups()
        self.questions()
        response = self.upvote()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("title", result.get("question")[0])

    def test_downvote_questions(self):
        """Test downvote questions endpoint"""
        self.meetups()
        self.questions()
        response = self.downvote()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("body", result.get("question")[0])
