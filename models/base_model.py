#!/usr/bin/env python3
from datetime import datetime
import json
from uuid import uuid4

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

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
