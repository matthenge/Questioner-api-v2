from app import create_app
from .base_tests import BaseTest
import json


class TestComments(BaseTest):
    """Test comments"""

    def test_post_comment(self):
        """Test create comment endpoint"""
        self.meetups()
        self.questions()
        response = self.comments()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 201)
        self.assertIn("title", result.get("data")[0])
