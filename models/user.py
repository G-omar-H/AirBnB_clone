#!/usr/bin/python3
"""
AirBnB cloning prototype project
"""
import models


class User(models.BaseModel):
    """
    sub User class inheriting from BaseModel paretn class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
