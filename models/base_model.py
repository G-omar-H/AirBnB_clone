#!/usr/bin/python3
"""
AirBnb clone project base file
"""
import uuid
import datetime

class BaseModel():
    """
    BaseModel that defines all common attributes/methods for other classes
    """
    
    
    def __init__(self):
        """
        initializing BaseModel public attributes
        args:
            @id: unique id for each basemodel
            @created_at: assign the current datetime when aninstance is created
            @updated_at: assign the current datetime when an instance is updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        a friendly string representation of the class
        """
        return "[{}] ({}) {}".format(self.__name__, self.id, self.__dict__)

    def save(self):
        """
        update the updated_at field when modification applyed to a class object instance
        """
        self.updated_at = datetime.datetime.now()
        return self.updated_at

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__
        my_dict[__class__] = self.__name__
        my_dict[created_at] = self.created_at.isoformat()
        my_dict[updated_at] = self.updated_at.isoformat()
        return my_dict

