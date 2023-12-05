import json


class FileStorage():
    """ Class To read/wrtie objects as json """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.id}"] = obj.to_dict()

    def save(self):
        with open(f"{self.__file_path}", 'w') as write_file:
            json.dump(self.__objects, write_file)

    def reload(self):
        try:
            with open(f"{self.__file_path}", 'r') as read_file:
                self.__objects = json.load(read_file)
        except FileNotFoundError:
            pass
