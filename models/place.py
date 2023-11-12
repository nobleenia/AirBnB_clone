#!/usr/bin/python3
"""
`Place` class, derived from the `BaseModel` class
Represents place objects and stores various information about places
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    `Place` class is a subclass of `BaseModel`
           represents place objects in the application

    Attributes:
        city_id (str): The ID of the city where the place is located
        user_id (str): The ID of the user who owns the place
        name (str): The name of the place
        description (str): A description of the place
        number_rooms (int): The number of rooms in the place
        number_bathrooms (int): The number of bathrooms in the place
        max_guest (int): The maximum guest capacity of the place
        price_by_night (int): The price per night for renting the place
        latitude (float): The latitude coordinate of the place's location
        longitude (float): The longitude coordinate of the place's location
        amenity_ids (list): A list of amenity IDs associated with the place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
