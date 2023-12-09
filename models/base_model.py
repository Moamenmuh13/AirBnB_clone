#!/usr/bin/env python
"""
        BaseModel Class
        all common attributes/methods for other classes
"""
import uuid
import datetime as dt


class BaseModel():
    """
        BaseModel Class
        all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """initialize BaseModel object"""
        self.id = str(uuid.uuid4())
        self.created_at = dt.datetime.now()
        self.updated_at = self.created_at
        from models import storage
        storage.new(self)
        # Note For anyone reading
        # The self here doesn't refer to the storage object
        # but the BaseModel one

        if kwargs:
            for key, value in kwargs.items():
                # if key == "__class__":
                #     continue
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, dt.datetime.fromisoformat(value))
                else:
                    self.__dict__[key] = kwargs[key]

    def __str__(self):
        """return the string representaion of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """wrtie the object to the json file"""
        self.updated_at = dt.datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """converts the attributes of the object to dict format"""
        info = dict()
        info = self.__dict__.copy()
        info["__class__"] = self.__class__.__name__
        info["created_at"] = self.created_at.isoformat()
        info["updated_at"] = self.updated_at.isoformat()
        return info
