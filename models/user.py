#!/usr/bin/python3
"""
AirBnB cloning prototype project
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """
    sub User class inheriting from BaseModel paretn class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
