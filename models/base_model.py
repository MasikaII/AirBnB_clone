#!/usr/bin/python3
"""
A module containing a base class
"""
from datetime import datetime
from uuid import uuid4
import json
from models.__init__.py import storage


class BaseModel:
    """ Describes the attibutes and methods of all other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or  key =="updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new()

    def __str__(self):
        """prints the string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(s)
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
