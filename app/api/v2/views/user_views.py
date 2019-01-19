from flask import jsonify, make_response, request
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from app.api.v2.models.user_models import UserModels
from app.api.v2.utils.utilities import Helpers

helpers = Helpers()


class Users(Resource):
    """Class for user registration"""

    def __init__(self):
        """Initialize the user class"""
        self.parser = RequestParser()
        self.parser.add_argument("firstname", type=str, required=True,
                                 help="please input a valid name")
        self.parser.add_argument("lastname", type=str, required=True,
                                 help="please input a valid name")
        self.parser.add_argument("othername", type=str, required=True,
                                 help="please input a valid name")
        self.parser.add_argument("email", type=str, required=True,
                                 help="please input an email")
        self.parser.add_argument("phoneNumber", type=str, required=True,
                                 help="please input a valid phone number")
        self.parser.add_argument("username", type=str, required=True,
                                 help="please input a username")
        self.parser.add_argument("password", type=str, required=True,
                                 help="please input a password")
        self.parser.add_argument("confirm_password", type=str, required=True,
                                 help="confirm your password")

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

        password = helpers.hash_password(password, username)
        confirm_password = helpers.hash_password(confirm_password, username)
        check = helpers.check_hash_password(password, confirm_password)
        if not check:
            return {
                "status": 403,
                "error": "Passwords do not match"
            }, 403

        newUser = UserModels(firstname, lastname, othername, email, username,
                             phoneNumber, password)
        newUser.signup()

        return {
            "status": 201,
            "data": [{
                "user": newUser.__dict__
            }]
        }, 201
