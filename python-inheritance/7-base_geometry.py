#!/usr/bin/python3
"Module that have a class with publics instances"


class BaseGeometry:
    "Class BaseGeometry (based on 6-base_geometry.py)."
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))