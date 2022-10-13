#!/usr/bin/python3
"Module that have a class with one public instance"


class BaseGeometry:
    "Public instance"
    def area(self):
        raise Exception("area() is not implemented")
