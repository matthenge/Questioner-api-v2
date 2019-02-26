"""Module for all User authentication"""
import datetime
import jwt
import os
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from functools import wraps
from flask import request, current_app, url_for
from flask_mail import Message
from app.api.v2.models.user_models import UserModels
from app.api.v2.utils.validator import Validators

validate = Validators()


class Authenticate:
    """Class to authenticate users"""

    def token_generator(self, username):
        """Method to generate token"""
        try:
            expiry = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
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

    def reset_token(self, username):
        """Function to generate reset password token"""
        s = Serializer(os.getenv("SECRET_KEY"), expires_in=3600)
        token = s.dumps({
            "username": username
        }).decode("UTF-8")
        return token

    @staticmethod
    def verify_token(token):
        """Verify reset password token"""
        s = Serializer(os.getenv("SECRET_KEY"))
        try:
            username = s.loads(token)["username"]
        except:
            return None
        return username


def login_required(fun):
    """User authentication decorator"""
    @wraps(fun)
    def authenticate(*args, **kwargs):
        """User authentication decorator"""
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            blacklisted = validate.blacklisted(token)
            if blacklisted:
                return {
                    "status": 401,
                    "error": "You are logged out. Please login again"
                }, 401
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
            user = validate.valid_user(data['username'])
            if user:
                return fun(*args, **kwargs, current_user=user)
            return {
                    "status": 404,
                    "error": "User not found"
                }, 404
        else:
            return {
                    "status": 401,
                    "error": "You are not logged in. Please login"
                }, 401
    return authenticate


def admin_required(fun):
    """Admin authentication decorator"""
    @wraps(fun)
    def admin_auth(*args, **kwargs):
        """Admin authentication decorator"""
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            blacklisted = validate.blacklisted(token)
            if blacklisted:
                return {
                    "status": 401,
                    "error": "You are logged out. Please login again"
                }
            try:
                data = jwt.decode(
                                    token,
                                    os.getenv("SECRET_KEY"),
                                    algorithm='HS256'
                                )
            except jwt.ExpiredSignatureError:
                return {
                    "status": 401,
                    "error": "Session expired. Please login again"
                }, 401
            except jwt.InvalidTokenError:
                return {
                    "status": 401,
                    "error": "Invalid token. Please login again"
                }, 401
            user = validate.valid_admin(data['username'])
            if user:
                return fun(*args, **kwargs, current_user=user)
            return {
                    "status": 401,
                    "error": "You are not authorized to perform this action"
                }, 401
        else:
            return {
                    "status": 401,
                    "error": "You are not logged in. Please login"
                }, 401
    return admin_auth


def send_mail(email, url, token):
    """Method to send user email"""
    msg = Message(
            "Password Reset Request",
            sender="noreply@questioner.com",
            recipients=[email])
    msg.body = f"""To reset your password, visit the following link:

{(url+token)}

If you did not make this request then ignore this email.
"""
    from app import mail
    mail.send(msg)
