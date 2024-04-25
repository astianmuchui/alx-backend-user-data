#!/usr/bin/env python3

"""
Mapping definition of a user model
using the sqlalchemy ORM
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR

Base = declarative_base()


class User(Base):

    """
    User model definition
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(250), nullable=False)
    email = Column(VARCHAR(250), nullable=False)
    hashed_password = Column(VARCHAR(250), nullable=False)
    session_id = Column(VARCHAR(250), nullable=True)
    reset_token = Column(VARCHAR(250), nullable=True)
