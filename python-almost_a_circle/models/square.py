#!/usr/bin/python3
"""Module that have a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self._size = size

    def __str__(self):
        """Square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size
                )

    @property
    def size(self):
        """Getter"""
        return self._size

    @size.setter
    def size(self, value):
        """Setter"""
        self.size = value
