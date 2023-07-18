#!/usr/bin/python3
""" class review"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    rep a review

    Attribute
    place_id
    user_id
    text
    """

    place_id = ""
    user_id = ""
    text = ""
