"""Module for all User authentication"""
import datetime
import jwt
import os
from functools import wraps
from flask import request, current_app
from app.api.v2.models.user_models import UserModels


class Authenticate:
    """Class to authenticate users"""

    def token_generator(self, username):
        """Method to generate token"""
        try:
            expiry = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            details = {
                'username': username,
                'exp': expiry
                }
            token = jwt.encode(
                                details,
                                os.getenv("SECRET_KEY"),
                                algorithm='HS256'
                            )
            return token
        except Exception as error:
            return str(error)

    def login_required(f):
        """User authentication decorator"""
        @wraps(f)
        def authenticate(*args, **kwargs):
            """User authentication decorator"""
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
                try:
                    data = jwt.decode(
                                        token,
                                        os.getenv("SECRET_KEY"),
                                        algorithm='HS256'
                                    )
                except jwt.ExpiredSignatureError:
                    return {
                        "status": 401,
                        "error": "Login expired. Please login again"
                    }, 401
                except jwt.InvalidTokenError:
                    return {
                        "status": 401,
                        "error": "Invalid authentication. Please login again"
                    }, 401
                return f(*args, **kwargs, current_user=data['username'])
            else:
                return {
                        "status": 401,
                        "error": "You are not logged in. Please login"
                    }, 401
        return authenticate

    def admin_required(self):
        """Admin authentication decorator"""
        @wraps(f)
        def admin_auth(*args, **kwargs):
            """Admin authentication decorator"""
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
                try:
                    data = jwt.decode(
                                        token,
                                        os.getenv("SECRET_KEY"),
                                        algorithm='HS256'
                                    )
                except jwt.ExpiredSignatureError:
                    return {
                        "status": 401,
                        "error": "Login expired. Please login again"
                    }, 401
                except jwt.InvalidTokenError:
                    return {
                        "status": 401,
                        "error": "Invalid token. Please login again"
                    }, 401
                user = UserModels.check_admin(self, data['username'])
                if user:
                    return f(*args, **kwargs, current_user=data['username'])
            else:
                return {
                        "status": 401,
                        "error": "You are not authorized\
                        to perform this action"
                    }, 401
        return admin_auth
