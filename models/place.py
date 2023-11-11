#!/usr/bin/python3
"""
AirBnb clone project place file
"""
import models


class Place(models.BaseModel):
	"""
	Place class that inherits from BaseModel
	"""

	city_id = ""
	user_id = ""
	name = ""
	description = ""
	number_rooms = 0
	number_bathrooms = 0
	max_guest = 0
	price_by_night = 0
	latitude = 0
	longitude = 0
	amenity_ids = []
