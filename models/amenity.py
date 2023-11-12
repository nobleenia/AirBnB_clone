#!/usr/bin/python3
"""
`Amenity` class, which is derived from the `BaseModel` class
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    The `Amenity` class is a subclass of `BaseModel`
        represents amenity objects in the application

    Attributes:
        name (str): The name of the amenity
    """
    name = ""
