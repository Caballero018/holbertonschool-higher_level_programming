#!/usr/bin/python3
"Module that have a class Student that defines a student by"


class Student:
    "Class Student that defines a student by"
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not attrs:
            attrs = self.__dict__
            return attrs
        else:
            ds = {}
            self = self.__dict__
            for ls in attrs:
                if not ls in self:
                    continue
                ds[ls] = self[ls]
            return ds
