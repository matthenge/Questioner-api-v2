"""Tests"""
import unittest
from app import create_app
from .base_tests import BaseTest
import json


class TestMeetups(BaseTest):
    """Test Meetups"""

    def test_post_meetup(self):
        """Test create meetup endpoint"""
        response = self.meetups()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 201)
        self.assertIn("topic", result.get("meetup"))

    def test_get_meetup(self):
        """Test get meetup endpoint"""
        self.meetups()
        response = self.get_meetups()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("location", result.get("meetups"))

    def test_get_upcoming_meetup(self):
        """Test get upcoming meetup endpoint"""
        self.meetups()
        response = self.get_upcoming_meetups()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("meetupid", result.get("meetups")[0])

    def test_get_upcoming_meetup(self):
        """Test delete meetup endpoint"""
        self.meetups()
        response = self.delete_meetup()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["data"], "Meetup deleted")

    def test_get_all_meetups(self):
        """Test get all meetups endpoint"""
        self.meetups()
        response = self.get_all_meetups()
        result = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("meetupid", result.get("data")[0])
