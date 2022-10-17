#!/usr/bin/python3
"Module that have a class Student that defines a student by"


class Student:
    "Class Student that defines a student by"
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            attrs = self.__dict__
            return attrs
        else:
            ds = {}
            self = self.__dict__
            for ls in attrs:
                if ls in self:
                    ds[ls] = self[ls]
                else:
                    continue
            return ds
    
    def reload_from_json(self, json):
        key = json.keys()
        self = self.__dict__
        for k in key:
            self[k] = json[k]
