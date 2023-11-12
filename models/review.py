#!/usr/bin/python3
"""
`Review` class, which is derived from the `BaseModel` class
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    The `Review` class is a subclass of `BaseModel`
        represents review objects in the application

    Attributes:
        place_id (str): The ID of the place being reviewed
        user_id (str): The ID of the user who wrote the review
        text (str): The text content of the review
    """
    place_id = ""
    user_id = ""
    text = ""
