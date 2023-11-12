#!/usr/bin/python3
"""
This script defines a base class, `BaseModel`
Serves as a foundation for other models in the AirBnB application
Includes methods for creating, saving, and representing objects
Converts methods to dictionary format for serialization
"""
import models
from uuid import uuid4
from datetime import datetime

datetime_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """
    The `BaseModel` class serves as the base class for other models
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the `BaseModel` class.

        Args:
            *args: Non-keyword arguments
            **kwargs: Keyword arguments used to populate the object's attributes

        Attributes:
            id (str): A universally unique identifier for the object
            created_at: A timestamp indicating when object was created
            updated_at: A timestamp indicating when object was last updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"], datetime_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"], datetime_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        A string representation of the object

        Returns:
            str: A string containing the class name, object's ID, and attributes
        """
        return ("[{}], ({}), {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates to current date and time and saves the object to storage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def __repr__(self):
        """
        Returns string representation of the object using `__str__` method
        """
        return (self.__str__())

    def to_dict(self):
        """
        Converts the object to a dictionary format for serialization

        Returns:
            new_dict: A dictionary representation of the object
        """
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, (datetime, )):
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        return new_dict
