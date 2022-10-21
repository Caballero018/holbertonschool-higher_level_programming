#!/usr/bin/python3
"Module that have a class named Base"
import json


class Base:
    "Class named Base"
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None:
            list_objs = cls.to_json_string([i.__dict__ for i in list_objs])
        else:
            list_objs = "[]"
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(list_objs)

    @staticmethod
    def from_json_string(json_string):
        if json_string is not None:
            return json.loads(json_string)
        else:
            return "[]"
