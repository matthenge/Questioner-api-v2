from app import create_app
from .base_tests import BaseTest
import json


class TestRsvps(BaseTest):
    """Test Rsvps"""

    def test_post_rsvp(self):
        """Test create rsvp endpoint"""
        self.meetups()
        response = self.post_rsvps()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 201)
        self.assertIn("topic", result.get("data")[0])

    def test_post_rsvp_nonexistent_meetup(self):
        """Test create rsvp to a nonexistent meetup"""
        self.meetups()
        response = self.post_rsvp_nonexistent_meetup()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(result["error"], "Meetup 20 does not exist")

    def test_post_rsvp_twice(self):
        """Test create rsvp twice"""
        self.meetups()
        self.post_rsvps()
        response = self.post_rsvps_twice()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 409)
        self.assertEqual(result["error"], "User 1 already reserved a spot")
