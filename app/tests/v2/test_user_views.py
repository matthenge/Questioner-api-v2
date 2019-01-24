"""User Tests"""
import unittest
from app import create_app
from .base_tests import BaseTest
import json

message = "Password must have 8 chars, digit, lower & upper case, symbol"


class TestUsers(BaseTest):
    """Test users"""

    def test_add_user(self):
        """Test user signup"""
        response = self.signup()
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn("data", result)

    def test_login(self):
        """Test user login endpoint"""
        self.signup()
        response = self.user_login()
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", result.get("data")[0])

    def test_repeat_username(self):
        """Test signup repeat username"""
        self.signup()
        response = self.signup()
        result = json.loads(response.data.decode())
        self.assertEqual(result["error"], "Username already exists")
        self.assertEqual(response.status_code, 400)

    def test_weak_password(self):
        """Test weak password"""
        response = self.weak_password()
        result = json.loads(response.data.decode())
        self.assertEqual(result["error"], message)
        self.assertEqual(response.status_code, 400)

    def test_invalid_email(self):
        """Test an invalid email"""
        response = self.invalid_email()
        result = json.loads(response.data.decode())
        self.assertEqual(result["error"],
                         "martingmail.com is not a valid email")
        self.assertEqual(response.status_code, 400)

    def test_empty_strings(self):
        """Test empty string inputs"""
        response = self.post_empty_string()
        result = json.loads(response.data.decode())
        self.assertEqual(result["error"], "'' does not seem like a valid name")
        self.assertEqual(response.status_code, 400)

    def test_no_user_login(self):
        """Test user login for an unregistered user"""
        self.signup()
        response = self.no_user_login()
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
