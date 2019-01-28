from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from app.api.v2.models.user_models import UserModels
from app.api.v2.utils.utilities import Helpers
from app.api.v2.utils.authentication import Authenticate
from app.api.v2.utils.validator import Validators
from app.api.v2.utils.authentication import admin_required
import json

helpers = Helpers()
auth = Authenticate()
validate = Validators()


class Users(Resource):
    """Class for user registration"""

    def __init__(self):
        """Initialize the user class"""
        self.parser = RequestParser()
        self.parser.add_argument("firstname", type=str, required=True,
                                 help="Firstname is missing")
        self.parser.add_argument("lastname", type=str, required=True,
                                 help="lastname is missing")
        self.parser.add_argument("othername", type=str, required=True,
                                 help="othername is missing")
        self.parser.add_argument("email", type=str, required=True,
                                 help="email is missing")
        self.parser.add_argument("phoneNumber", type=str, required=True,
                                 help="phoneNumber is missing")
        self.parser.add_argument("username", type=str, required=True,
                                 help="Username is missing")
        self.parser.add_argument("password", type=str, required=True,
                                 help="password is missing")
        self.parser.add_argument("confirm_password", type=str, required=True,
                                 help="confirm password is missing")

    def post(self):
        """Register user endpoint"""
        args = self.parser.parse_args()
        args = request.get_json()
        firstname = args["firstname"]
        lastname = args["lastname"]
        othername = args["othername"]
        email = args["email"]
        phoneNumber = args["phoneNumber"]
        username = args["username"]
        password = args["password"]
        confirm_password = args["confirm_password"]

        if validate.valid_inputs(firstname, lastname, othername):
            return validate.valid_inputs(firstname, lastname, othername)
        if validate.valid_phone(phoneNumber):
            return validate.valid_phone(phoneNumber)
        if validate.user_validator(email, password, username):
            return validate.user_validator(email, password, username)
        if validate.user_exists(email, username):
            return validate.user_exists(email, username)
        password = helpers.hash_password(password, username)
        confirm_password = helpers.hash_password(confirm_password, username)
        check = helpers.check_hash_password(password, confirm_password)
        if not check:
            return {
                "status": 400,
                "error": "Passwords do not match"
            }, 400

        newUser = UserModels(firstname, lastname, othername, email, username,
                             phoneNumber, password)
        user = newUser.signup()
        user = json.loads(user)
        token = auth.token_generator(username)
        return {
            "status": 201,
            "data": [{
                "token": token.decode('UTF-8'),
                "user": user
            }]
        }, 201


class UserLogin(Resource):
    """Class to login user"""
    def __init__(self):
        """Initialize the login class"""
        self.parser = RequestParser()
        self.parser.add_argument("username", type=str, required=True,
                                 help="please input a username")
        self.parser.add_argument("password", type=str, required=True,
                                 help="please input a password")

    def post(self):
        """method to login user"""
        data = self.parser.parse_args()
        data = request.get_json()
        userName = data["username"]
        passWord = data["password"]

        hashed = helpers.hash_password(passWord, userName)
        user = UserModels.check_username(self, userName)
        if user:
            check = helpers.check_hash_password(user["password"], hashed)
            if check is True:
                token = auth.token_generator(user["username"])
                return {
                    "status": 200,
                    "data": [{
                        "token": token.decode('UTF-8'),
                        "user": user
                    }]
                }, 200
            return {
                    "status": 404,
                    "error": "Wrong password"
            }, 401
        return {
            "status": 404,
            "error": "user not found: Please register"
        }, 404


class Promote(Resource):
    """Class to promote user role"""

    @admin_required
    def put(self, userId, current_user):
        """Promote normal user to admin status"""
        user = UserModels.promote_user(self, userId)
        user = json.loads(user)
        if not user:
            return {
                "status": 404,
                "error": "User {} not found".format(userId)
            }, 404
        return {
            "status": 200,
            "data": user
        }, 200
