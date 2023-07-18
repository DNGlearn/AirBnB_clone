#!/usr/bin/python3
""" class place """
from models.base_model import BaseModel

class Place(BaseModel):
    """
    rep place

    Attribute
    city_id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    ameninty_ids = ""
