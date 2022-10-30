#!/usr/bin/python3
"""
contains a class that serialises instances to a json file and
deserialises json files to instances
"""


import json
from models.base_model import BaseModel


class FileStorage():
    """ serializes instances to a JSON file and
    deserializes JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
        # FileStorage.__objects["{}.{}".format(key, obj.id)] = obj
        # return f"Filestorage.__objects {key}.{obj.id}" = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            new_dict = FileStorage.__objects.copy()
            for key, value in FileStorage.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """Deserialise the JSON in __file_path if it exists"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
                for base_dict in loaded.values():
                    name = base_dict["__class__"]
                    del base_dict["__class__"]
                    # new_obj = BaseModel(**base_dict)
                    self.new(eval(name)(**base_dict))
        except FileNotFoundError:
            return
