#!/usr/bin/env python3
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """Hashes a password with bcrypt
    """
    return hashpw(password.encode('utf-8'), gensalt())
