#!/usr/bin/python3
""" User Class"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    A User

    Attributes:
    email
    pass
    f_name
    l_name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
