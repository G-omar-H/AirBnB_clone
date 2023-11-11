#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
<<<<<<< HEAD
=======
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

>>>>>>> origin/pixi

storage = FileStorage()
storage.reload()
