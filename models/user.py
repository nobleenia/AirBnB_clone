#!/usr/bin/python3
"""
User class, which is derived from the BaseModel class
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    The `User` class is a subclass of `BaseModel`
         represents application  user objects

    Attributes:
        email (str): The email address of the user
        password (str): The user's password
        first_name (str): The first name of the user
        last_name (str): The last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
