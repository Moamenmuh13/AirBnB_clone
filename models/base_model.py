#!/usr/bin/env python
import uuid
import datetime as dt


class BaseModel():
    """
        BaseModel Class
        all common attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = dt.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"{self.__class__.__name__} ({self.id} {self.__dict__})"

    def save(self):
        self.updated_at = dt.datetime.now()

    def to_dict(self):
        info = dict()
        info = self.__dict__.copy()
        info["__class__"] = self.__class__.__name__
        info["created_at"] = self.created_at.isoformat()
        info["updated_at"] = self.updated_at.isoformat()
        return info
