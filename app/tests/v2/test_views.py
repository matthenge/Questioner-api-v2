"""Tests"""
import unittest
from app import create_app
from .base_tests import BaseTest
import json

message = "Password must have 8 chars, digit, lower & upper case, symbol"


class TestViews(BaseTest):
    """Test views"""

    def test_login(self):
        """Test user login endpoint"""
        self.signup()
        response = self.user_login()
        self.assertEqual(response.status_code, 200)

    def test_create_meetup(self):
        """Test create meetup endpoint"""
        self.register()
        response = self.create_meetup()
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Meetup Created Successfully")
        self.assertEqual(response.status_code, 201)

    def test_get_meetup(self):
        """Test get specific meetup endpoint"""
        response = self.get_meetup()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Message"], "Success")
        self.assertEqual(response.status_code, 200)

    def test_get_nonexistent_meetup(self):
        """Test get nonexistent meetup"""
        response = self.get_nonexistent_meetup()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Error"], "Meetup does not exist")
        self.assertEqual(response.status_code, 404)

    def test_get_all_meetups(self):
        """Test get all meetups endpoint"""
        self.register()
        self.create_meetup()
        response = self.get_all_meetups()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Message"], "Success")
        self.assertEqual(response.status_code, 200)

    def test_post_question(self):
        """Test post question endpoint"""
        self.create_meetup()
        response = self.post_question()
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Question Posted Successfully")
        self.assertEqual(response.status_code, 201)

    def test_upvote_question(self):
        """Test Upvote question endpoint"""
        self.post_question()
        response = self.upvote_question()
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Upvote Successful")
        self.assertEqual(response.status_code, 200)

    def test_downvote_question(self):
        """Test Downvote question endpoint"""
        self.post_question()
        self.upvote_question()
        response = self.downvote_question()
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Downvote Successful")
        self.assertEqual(response.status_code, 200)

    def test_reserve_space(self):
        """Test RSVP endpoint"""
        self.create_meetup()
        response = self.reserve_space()
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "RSVP created")
        self.assertEqual(response.status_code, 201)

    def test_repeat_username(self):
        """Test signup repeat username"""
        response = self.signup()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Error"], "Username already exists")
        self.assertEqual(response.status_code, 403)

    def test_weak_password(self):
        """Test weak password"""
        response = self.weak_password()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Error"], message)
        self.assertEqual(response.status_code, 403)

    def test_past_meetup_date(self):
        """Test past meetup date"""
        response = self.past_meetupdate()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Error"], "New Meetup cannot be in the past")
        self.assertEqual(response.status_code, 403)

    def test_invalid_email(self):
        """Test an invalid email"""
        response = self.invalid_email()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Error"],
                         "martingmail.com is not a valid email")
        self.assertEqual(response.status_code, 403)

    def test_get_upcoming_meetup(self):
        """Test fetch upcoming meetups"""
        self.future_meetups()
        response = self.get_all_upcoming_meetups()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Message"],
                         "Success")
        self.assertEqual(response.status_code, 200)

    def test_empty_strings(self):
        """Test empty string inputs"""
        self.create_meetup()
        response = self.post_empty_string()
        result = json.loads(response.data.decode())
        self.assertEqual(result["title"], "Field cannot be empty")
        self.assertEqual(response.status_code, 400)

    def test_no_user_login(self):
        """Test user login for an unregistered user"""
        self.signup()
        response = self.no_user_login()
        result = json.loads(response.data.decode())
        self.assertEqual(result["Error"], "User not found: Please register")
        self.assertEqual(response.status_code, 404)
