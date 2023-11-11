#!/usr/bin/python3
"""
AirBnb clone project city file
"""
import models


class City(models.BaseModel):
	"""
	city class that inherits from BaseModel
	"""

	name = ""
	state_id = ""

