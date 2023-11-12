#!/usr/bin/python3
"""
`State` class, which is derived from the `BaseModel` class
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    The `State` class is a subclass of `BaseModel`
         and represents state objects in the application

    Attributes:
        name (str): The name of the state
    """
    name = ""
