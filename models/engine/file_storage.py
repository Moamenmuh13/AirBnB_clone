#!/usr/bin/env python
"""
FileStorage Module
serializes/deserializes the object of the app to json file
"""
import json
from ..base_model import BaseModel
from ..user import User
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State


class FileStorage:
    """Class To read/wrtie objects as json"""

    def __init__(self):
        """intitialize Class Object"""
        self.__file_path = "file.json"
        self.__objects = dict()

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "Amenity": Amenity,
                   "City": City,
                   "Place": Place,
                   "Review": Review,
                   "State": State
                   }
        return classes

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as write_file:
            d = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(d, write_file)

    def reload(self):
        """ deserializes the JSON file to __objects \
            (only if the JSON file (__file_path) exists ;\
             otherwise, do nothing. If the file doesn’t exist, \
            no exception should be raised"""
        try:
            with open(f"{self.__file_path}", 'r') as read_file:
                obj_dict = json.load(read_file)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
            self.__objects = obj_dict
        except FileNotFoundError:
            pass
