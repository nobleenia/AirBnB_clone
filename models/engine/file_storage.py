#!/usr/bin/python3
"""
`FileStorage` class responsible for managing and persisting data to a JSON file.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage():
    """
    `FileStorage` class responsible for managing and persisting objects to a JSON file
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review,
        "State": State
    }

    def all(self):
        """
        Returns a dictionary of all objects currently loaded in memory

        Returns:
            dict: A dictionary containing objects with keys 
                  in "Classname.object_id" and values object instances
        """
        return self.__objects

    def new(self, obj):
        """
        Adds new object to the in-memory dictionary of objects

        Args:
            obj: An instance of a class derived from BaseModel added to the dictionary
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Saves current in-memory objects to a JSON file by converting to dictionary form
        """
        new_obj_dict = {}
        for key, obj in self.__objects.items():
            new_obj_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(new_obj_dict, f)

    def reload(self):
        """
        Loads objects from JSON file and populates in-memory dictionary with loaded objects
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_load = json.load(f)
            for key, value in obj_load.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
