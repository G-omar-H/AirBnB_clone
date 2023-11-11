#!/usr/bin/python3
"""
AirBnb clone project review file
"""
import models


class Review(models.BaseModel):
    """
    Review class that inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
    