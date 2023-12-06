import json


class FileStorage:
    """Class To read/wrtie objects as json"""

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}
        return classes

    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as write_file:
            d = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(d, write_file)

    def reload(self):
        try:
            with open(f"{self.__file_path}", 'r') as read_file:
                obj_dict = json.load(read_file)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
            self.__objects = obj_dict

        except FileNotFoundError:
            pass

    def classes(self):
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}

        return classes
