#!/user/bin/python3
"""
AirBnb clone project amenity file
"""
from models import BaseModel


class Amenity(BaseModel):
	"""
	Amenity class that inherits from BaseModel
	"""

	name = ""

	def __init__(self):
		"""
		Amenity initialiser
		"""
		super().__init__(self)
