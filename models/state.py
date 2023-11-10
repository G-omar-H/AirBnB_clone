#!/usr/bin/python3
"""
AirBnb clone project state file
"""
from models import BaseModel


class State(BaseModel):
	"""
	State class that inherits from BaseModel
	"""

	name = ""

	def __init__(self):
		"""
		State initialiser
		"""
		super().__init__(self)
