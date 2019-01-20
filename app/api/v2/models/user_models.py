"""Module for user operations"""
from .base_models import BaseModels
from app.api.v2.utils.utilities import Helpers

helpers = Helpers()


class UserModels(BaseModels):
    """Class for user CRUD operations"""

    def __init__(self, firstname, lastname, othername, email, username,
                 phoneNumber, password):
        """Initialize the users models"""
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.password = password

    def signup(self):
        """method for user signup"""
        user_details = dict(
            firstname=self.firstname,
            lastname=self.lastname,
            othername=self.othername,
            email=self.email,
            phoneNumber=self.phoneNumber,
            username=self.username,
            password=self.password
        )
        table = "users"
        columns = ", ".join(user_details.keys())
        values = "', '".join(map(str, user_details.values()))
        details = {
            "firstname": "firstname",
            "lastname": "lastname",
            "phoneNumber": "phoneNumber",
            "username": "username"
        }
        data = ",".join(map(str, details.values()))
        user = BaseModels.save_data(self, table, columns, values, data)

        return user

    def check_username(self, userName):
        """Method to retrieve username"""
        table = "users"
        columns = "userId, firstname, lastname, username, password, email"
        column = "username"
        user = BaseModels.fetch_specific(self, columns, table, column,
                                         userName)
        return user