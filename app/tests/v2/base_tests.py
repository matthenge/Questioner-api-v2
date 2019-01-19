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

        self.meetup = {
            "location": "Kisumu",
            "images": "www.image1.com",
            "topic": "data science",
            "happeningOn": "2019-10-22 10:00",
            "userId": 1
        }
        self.oneMeetup = {
            "location": "Kisumu",
            "images": "www.image1.com",
            "topic": "data science",
            "happeningOn": "2018-10-22 10:00",
            "userId": 1
        }
        self.duplicateuser = {
            "email": "general@gmail.com",
            "username": "genmatheng",
            "password": "Qwerty123!",
            "confirm_password": "Qwerty123!"
        }
        self.admin = {
            "firstname": "Nelson",
            "lastname": "Mandela",
            "othername": "lohilala",
            "email": "martin@gmail.com",
            "phoneNumber": "0711333666",
            "username": "martial",
            "password": "Qwerty123!",
            "confirm_password": "Qwerty123!"
        }
        self.email = {
            "email": "martingmail.com",
            "username": "martial",
            "password": "Qwerty123!",
            "confirm_password": "Qwerty123!"
        }
        self.question = {
            "createdBy": 1,
            "meetupId": 1,
            "title": "What is data science",
            "body": "please explain data science in length"
        }
        self.emptyStrings = {
            "createdBy": 1,
            "meetupId": 1,
            "title": " ",
            "body": "please explain data science in length"
        }
        self.rsvp = {
            "userId": 1
        }
        self.login = {
            "username": "genmatheng",
            "password": "Qwerty123!"
        }
        self.noUser = {
            "username": "dedan",
            "password": "kimathi"
        }
        self.weakpass = {
            "email": "martin@gmail.com",
            "username": "martial",
            "password": "qwerty123",
            "confirm_password": "qwerty123"
        }
        self.upcoming = {
            "location": "Kisumu",
            "images": "www.image1.com",
            "topic": "data science",
            "happeningOn": "2020-10-22 10:00",
            "userId": 1
        }

    def signup(self):
        """user registration"""
        res = self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(self.duplicateuser),
            content_type='application/json')
        return res

    def create_meetup(self):
        """meetup creation"""
        res = self.client.post(
            '/api/v2/meetups',
            data=json.dumps(self.meetup),
            content_type='application/json')
        return res

    def post_question(self):
        """post question"""
        res = self.client.post(
            '/api/v2/questions',
            data=json.dumps(self.question),
            content_type='application/json')
        return res

    def post_empty_string(self):
        """post question with empty fields"""
        res = self.client.post(
            '/api/v2/questions',
            data=json.dumps(self.emptyStrings),
            content_type='application/json')
        return res

    def reserve_space(self):
        """reserve attendance"""
        res = self.client.post(
            '/api/v2/meetups/1/rsvps',
            data=json.dumps(self.rsvp),
            content_type='application/json')
        return res

    def get_meetup(self):
        """Fetch specific meetup"""
        res = self.client.get(
            '/api/v2/meetups/1')
        return res

    def get_nonexistent_meetup(self):
        """Fetch meetup that does not exist"""
        res = self.client.get(
            '/api/v2/meetups/10')
        return res

    def get_all_meetups(self):
        """Fetch all meetups"""
        res = self.client.get(
            '/api/v2/meetups')
        return res

    def get_all_upcoming_meetups(self):
        """Fetch all upcoming meetups"""
        res = self.client.get(
            '/api/v2/meetups/upcoming')
        return res

    def upvote_question(self):
        """Upvote a question"""
        res = self.client.patch(
            '/api/v2/questions/1/upvote')
        return res

    def downvote_question(self):
        """Downvote a question"""
        res = self.client.patch(
            '/api/v2/questions/1/downvote')
        return res

    def user_login(self):
        """login user"""
        res = self.client.post(
            '/api/v2/auth/users/login',
            data=json.dumps(self.login),
            content_type='application/json')
        return res

    def register(self):
        """user registration"""
        res = self.client.post(
            '/api/v2/auth/users',
            data=json.dumps(self.admin),
            content_type='application/json')
        return res

    def weak_password(self):
        """user registration"""
        res = self.client.post(
            '/api/v2/auth/users',
            data=json.dumps(self.weakpass),
            content_type='application/json')
        return res

    def past_meetupdate(self):
        """Past happeningOn date"""
        res = self.client.post(
            '/api/v2/meetups',
            data=json.dumps(self.oneMeetup),
            content_type='application/json')
        return res

    def invalid_email(self):
        """inavlid email"""
        res = self.client.post(
            '/api/v2/auth/users',
            data=json.dumps(self.email),
            content_type='application/json')
        return res

    def future_meetups(self):
        """Past happeningOn date"""
        res = self.client.post(
            '/api/v2/meetups',
            data=json.dumps(self.upcoming),
            content_type='application/json')
        return res

    def no_user_login(self):
        """Non-existent user login"""
        res = self.client.post(
            '/api/v2/auth/login',
            data=json.dumps(self.noUser),
            content_type='application/json')
        return res

    def post_comment(self):
        """Post a comment"""
        res = self.client.post(
            '/api/v2/comments',
            data=json.dumps(self.question),
            content_type='application/json')
        return res

    def tearDown(self):
        """Method to destroy test database tables"""
        QuestionerDB.drop_tables()
