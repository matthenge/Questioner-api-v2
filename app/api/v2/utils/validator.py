"""Validators"""
import datetime
import re
from app.api.v2.models.user_models import UserModels

message = "Password must have 8 chars, digit, lower & upper case, symbol"
rex = re.compile(r"^(\s|\S)*(\S)+(\s|\S)*$")


class Validators():
    """Class for validations"""

    def valid_email(self, email):
        """Method to validate email"""
        ex = re.compile(r"(^[a-zA-Z0-9_+-]+(\.[0-9a-zA-Z_-]+)*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not re.match(ex, email):
            return {
                "status": 400,
                "error": "{} is not a valid email".format(email)
            }, 400

    def valid_password(self, password):
        """
        Validate password strength
        Should contain: Atleats 8 characters in length,
                    Atleast 1 uppercase letter,
                    Atleast 1 lowercase letter,
                    Atleast 1 digit,
                    Atleast one special character
        """
        regex = re.compile(r"^(?=.*[!@#$%^?&*()])(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.{8,})")
        if not re.search(regex, password):
            return {
                "status": 400,
                "error": message
            }, 400

    def valid_username(self, username):
        """Username should be atleast 3 characters long"""
        if len(username) < 3:
            return {
                "status": 400,
                "error": "Username is too short"
            }, 400

    def user_validator(self, email, password, username):
        """Validator for correct email, username and password"""
        if Validators().valid_email(email):
            return Validators().valid_email(email)
        if Validators().valid_password(password):
            return Validators().valid_password(password)
        if Validators().valid_username(username):
            return Validators().valid_username(username)

    def user_exists(self, email, username):
        """Validator to find if username and email already registered"""
        name = UserModels.check_username(self, username)
        mail = UserModels.check_email(self, email)
        if name:
            return {
                "status": 400,
                "error": "Username already exists"
            }, 400
        if mail:
            return {
                "status": 400,
                "error": "Email already exists"
            }, 400

    def valid_strings(self, *args):
        """Function to restrict empty strings"""
        for arg in args:
            if not re.match(rex, arg):
                return {
                    "status": 400,
                    "error": "comment field cannot empty"
                }, 400

    def valid_location(self, location):
        """Function to restrict empty location"""
        if not re.match(rex, location):
            return {
                    "status": 400,
                    "error": "location cannot be empty"
                }, 400

    def valid_topic(self, topic):
        """Function to restrict empty topic"""
        if not re.match(rex, topic):
            return {
                    "status": 400,
                    "error": "topic cannot be empty"
                }, 400

    def valid_inputs(self, *args):
        """Function to validate user inputs"""
        regex = re.compile(r"^[a-zA-Z]+(([',.-][a-zA-Z ])?[a-zA-Z]*)*$")
        for arg in args:
            if not re.match(regex, arg):
                return {
                    "status": 400,
                    "error": "'{}' does not seem like a valid name".format(arg)
                }, 400

    def valid_title(self, title):
        """Function to validate title"""
        if not re.match(rex, title):
            return {
                    "status": 400,
                    "error": "title cannot be empty"
                }, 400

    def valid_body(self, body):
        """Function to validate question body"""
        if not re.match(rex, body):
            return {
                    "status": 400,
                    "error": "body cannot be empty"
                }, 400

    def valid_time(self, happeningOn):
        """Method to validate happeningOn date"""
        createdOn = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        if happeningOn < createdOn:
            return {
                "status": 400,
                "error": "New Meetup cannot happen in the past"
            }, 400

    def valid_admin(self, username):
        """Validate admin"""
        user = UserModels.check_admin(self, username)
        return user

    def valid_user(self, username):
        """Validate user"""
        user = UserModels.check_username(self, username)
        return user

    def valid_response(self, response):
        """Method to validate response"""
        responses = ['no', 'yes', 'maybe']
        if response not in responses:
            return {
                "status": 400,
                "error": "Response is either 'yes', 'no' or 'maybe'"
            }, 400

    def valid_phone(self, phoneNumber):
        """Validate phone number"""
        regex = re.compile(r"^\+?[0-9]{3}-?[0-9]{6,15}$")
        if not re.match(regex, phoneNumber):
            return {
                "status": 400,
                "error": "'{}' is not a valid phone number".format(phoneNumber)
            }, 400

    def valid_date(self, date):
        """Validate the date entered"""
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
        except ValueError as e:
            return {
                "status": 400,
                "error": "Please use (yyyy-mm-dd hh:mm) format"
            }, 400
