#!/usr/bin/env python3
from bcrypt import hashpw, gensalt
from db import DB


def _hash_password(password: str) -> str:
    """Hashes a password with bcrypt
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> None:
        """Registers a new user
        """
        hashed_password = _hash_password(password)
        self._db.add_user(email, hashed_password)
