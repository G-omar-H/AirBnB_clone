#!/usr/bin/python3
"""
AirBnb clone project city file
"""
from models import BaseModel


class City(BaseModel):
	"""
	city class that inherits from BaseModel
	"""

	name = ""
	state_id = ""

	def __init__(self):
		"""
		city initialiser
		"""
		super().__init__(self)
