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
        return json.dumps(list_dictionaries)
