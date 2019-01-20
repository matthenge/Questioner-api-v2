"""Set up test base"""
import unittest
from app import create_app
import json
from app.database import QuestionerDB


class BaseTest(unittest.TestCase):
    """Test views"""

    def setUp(self):
        """Set up test variables"""
        self.app = create_app(configuration="testing")
        self.client = self.app.test_client()
        self.app_context = self.app
        self.app.testing = True

        self.oneUser = {
            "firstname": "Nelson",
            "lastname": "Mandela",
            "othername": "lohilala",
            "email": "martin@gmail.com",
            "phoneNumber": "0711333666",
            "username": "martial",
            "password": "Qwerty123!",
            "confirm_password": "Qwerty123!"
        }
        self.admin = {
            "firstname": "Nelson",
            "lastname": "Mandela",
            "othername": "lohilala",
            "email": "marn@gmail.com",
            "phoneNumber": "0711333666",
            "username": "pogba",
            "password": "Qwerty123!",
            "confirm_password": "Qwerty123!"
        }
        self.email = {
            "firstname": "Nelson",
            "lastname": "Mandela",
            "othername": "lohilala",
            "email": "martingmail.com",
            "phoneNumber": "0711333666",
            "username": "nelly",
            "password": "Qwerty123!",
            "confirm_password": "Qwerty123!"
        }
        self.emptyStrings = {
            "firstname": "Nelson",
            "lastname": "",
            "othername": "",
            "email": "tata@gmail.com",
            "phoneNumber": "0711333666",
            "username": "tata",
            "password": "Qwerty123!",
            "confirm_password": "Qwerty123!"
        }
        self.login = {
            "username": "martial",
            "password": "Qwerty123!"
        }
        self.noUser = {
            "username": "putin",
            "password": "Qwerty123!"
        }
        self.weakpass = {
            "firstname": "Nelson",
            "lastname": "Mandela",
            "othername": "lohilala",
            "email": "lucas@gmail.com",
            "phoneNumber": "0711333777",
            "username": "torreira",
            "password": "qwerty",
            "confirm_password": "qwerty"
        }

    def signup(self):
        """user registration"""
        res = self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(self.oneUser),
            content_type='application/json')
        return res

    def post_empty_string(self):
        """post question with empty fields"""
        res = self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(self.emptyStrings),
            content_type='application/json')
        return res

    def user_login(self):
        """login user"""
        res = self.client.post(
            '/api/v2/auth/login',
            data=json.dumps(self.login),
            content_type='application/json')
        return res

    def register(self):
        """user registration"""
        res = self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(self.admin),
            content_type='application/json')
        return res

    def weak_password(self):
        """user registration"""
        res = self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(self.weakpass),
            content_type='application/json')
        return res

    def invalid_email(self):
        """inavlid email"""
        res = self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(self.email),
            content_type='application/json')
        return res

    def no_user_login(self):
        """Non-existent user login"""
        res = self.client.post(
            '/api/v2/auth/login',
            data=json.dumps(self.noUser),
            content_type='application/json')
        return res

    def tearDown(self):
        """Method to destroy test database tables"""
        QuestionerDB.drop_tables()
