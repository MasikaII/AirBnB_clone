#!/usr/bin/python3
""" Class FileStorage used to serialize instances to json file
and to deserializes json file to instances"""


import json
from models.base_model import BaseModel


class FileStorage():
    """Serializes instances to json file and desrializes json file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key == obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FilesStorage.__file_path, "w", encoding="utf-8") as f:
            new_dict = FileStorage.__objects.copy()
            for key, value in FileStorage.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                for base_dict in  loaded.values():
                    name = base_dict["__class__"]
                    del base_dict["__class__"]
                    self.new(eval(name)(**base_dict))
        except FileNotFoundError:
            return
