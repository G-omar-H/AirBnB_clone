#!/usr/bin/python3
"""
convert data into JSON's standard\
    representation of datastructure
and strore into a file
"""
import json
import models
import re


class FileStorage:
    """
    class FileStorage that serializes instances\
        to a JSON file and\
            deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_id = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_id] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        temp = {}
        for key, value in self.__objects.items():
            if type(value) is not dict:
                temp[key] = value.to_dict()
            else:
                temp[key] = value
        with open(self.__file_path, "w", encoding="UTF8") as fd:
            json.dump(temp, fd)

    def reload(self):
        """
        deserializes the JSON file to __objects\
            (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If\
                the file doesn’t exist, no exception should be raised)
        """

        cls_dict = {
            "BaseModel": models.BaseModel,
            "User": models.User,
            "State": models.State,
            "City": models.City,
            "Amenity": models.Amenity,
            "Place": models.Place,
            "Review": models.Review,
        }

        try:
            with open(self.__file_path, "r", encoding="UTF8") as fd:
                temp = json.load(fd)
            for key, value in temp.items():
                key_pattern = re.compile(r"^([^\.]+)\.")

                match = key_pattern.match(key)
                cls_name = match.group(1)
                obj = cls_dict[cls_name](**value)
                self.new(obj)
        except IOError:
            pass
