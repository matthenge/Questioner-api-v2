"""Module for shared resources"""
import hashlib


class Helpers:
    """Helper methods"""

    def hash_password(self, password, username):
        """method to hash user passwords"""
        salt = password + username
        hashed = hashlib.md5(str.encode(salt)).hexdigest()
        return hashed

    def check_hash_password(self, password, hashed):
        """Compare hashed passwords"""
        if password == hashed:
            return True
