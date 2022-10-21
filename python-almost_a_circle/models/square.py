#!/usr/bin/python3
"""Module that have a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
                )

    @property
    def size(self):
        """
        Size
        """
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """
        args
        """
        if args:
            self = self.__dict__
            try:
                i = 0
                for k in self.keys():
                    if k == "_Rectangle__height":
                        continue
                    self[k] = args[i]
                    i += 1
            except IndexError:
                i = i - 1
        if kwargs:
            if not args:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        self = self.__dict__
        key = self.copy().keys()
        for k in key:
            if k == '_Rectangle__width':
                self["size"] = self[k]
                del self[k]
            if k == '_Rectangle__height':
                del self[k]
            if k == '_Rectangle__x':
                self["x"] = self[k]
                del self[k]
            if k == '_Rectangle__y':
                self["y"] = self[k]
                del self[k]
        return self
