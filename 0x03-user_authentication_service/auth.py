#!/usr/bin/env python3
from bcrypt import hashpw, gensalt
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """Hashes a password with bcrypt
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user
        """

        if self._db.find_user_by(email=email) is not None:
            raise ValueError(f"User {email} already exists")
        else:
            hashed_password = _hash_password(password)
            return User(email, hashed_password)
