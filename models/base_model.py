#!/usr/bin/env python3
#this class Base model defines all common attributes methods for other classes
from datetime import datetime
import json
from uuid import uuid4

class BaseModel:
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
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """Updates 'updated_at' current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns dictionary containing all keys/values"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
