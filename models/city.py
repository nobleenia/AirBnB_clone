#!/usr/bin/python3
"""
`City` class, which is derived from the `BaseModel` class
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    The `City` class is a subclass of `BaseModel`
         represents city objects in the application

    Attributes:
        state_id (str): The ID of the state to which the city belongs
        name (str): The name of the city
    """
    state_id = ""
    name = ""
