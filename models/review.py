#!/usr/bin/python3
"""
AirBnb clone project review file
"""
from models import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self):
        """
        Review initialiser
        """
        super().__init__(self)
    