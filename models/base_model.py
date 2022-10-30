#!/usr/bin/env python3
"""
A module containing the base class
"""


from datetime import datetime
from uuid import uuid4
import json
import models


class BaseModel:
    """
    The base class that defines the common attributes for other classes
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwars.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class_":
                        continue
                setattr(self, key, value)
            else:
                self.id = str(uuid4())
                self.created_at = datetime.today()
                self.updated_at = datetime.today()
                storage.new(self)

    def __str__(self):
        """
        Formats the output of class to_dict
        """
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """
        Updates 'updated_at' current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary containing all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
