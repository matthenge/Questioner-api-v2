"""Module for user operations"""
from .base_models import BaseModels
from app.api.v2.utils.utilities import Helpers
import json

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
            "email": "email",
            "phoneNumber": "phoneNumber",
            "username": "username"
        }
        data = ",".join(map(str, details.values()))
        user = BaseModels.save_data(self, table, columns, values, data)
        user = json.dumps(user, default=str)
        return user

    def check_username(self, userName):
        """Method to retrieve username"""
        table = "users"
        columns = "userId, firstname, lastname, username, password, email"
        column = "username"
        user = BaseModels.fetch_specific(self, columns, table, column,
                                         userName)
        return user

    def check_admin(self, userName):
        """Method to check if user in an admin"""
        table = "users"
        columns = "userId, isAdmin"
        column = "username"
        user = BaseModels.fetch_specific(self, columns, table, column,
                                         userName)
        if user["isadmin"] is True:
            return user

    def check_email(self, mail):
        """Method to check email"""
        table = "users"
        columns = "userId, email, username"
        column = "email"
        user = BaseModels.fetch_specific(self, columns, table, column,
                                         mail)
        return user

    def promote_user(self, userId):
        """Method to promote user to admin role"""
        table = "users"
        columns = "isAdmin=True"
        column = "userId"
        data = "userId, firstname, lastname, username, isAdmin"
        search_item = userId
        BaseModels.update_record(self, table, columns, column,
                                 search_item)
        user = BaseModels.fetch_specific(self, data, table, column,
                                         search_item)
        user = json.dumps(user, default=str)
        return user

    def reset_password(self, userName, password):
        """Method to promote user to admin role"""
        table = "users"
        columns = "password='{}'".format(password)
        column = "username"
        data = "userId, email, username"
        search_item = userName
        BaseModels.update_record(self, table, columns, column,
                                 search_item)
        user = BaseModels.fetch_specific(self, data, table, column,
                                         search_item)
        user = json.dumps(user, default=str)
        return user

    def logout_user(self, userId, token):
        """Method to logout user"""
        table = "blacklist"
        columns = "userId, token"
        data = "loggedOutAt"
        user = BaseModels.insert_data(self, table, columns, userId, token,
                                      data)
        return user

    def check_blacklisted(self, token):
        """Method to check blacklisted tokens"""
        table = "blacklist"
        columns = "loggedOutAt"
        column = "token"
        search_item = token
        token = BaseModels.fetch_specific(self, columns, table, column,
                                          search_item)
        return token
