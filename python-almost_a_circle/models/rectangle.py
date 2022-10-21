#!/usr/bin/python3
"""Module that have a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of the rectantgle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width of the rectantgle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Public method def that returns the area value of the
        Rectangle instance.
        """
        return self.__height * self.__width

    def display(self):
        """
        Public method def to print in stdout the Rectangle
        instance with the character # by taking care of x and y
        """
        if self.__height == 0 or self.width == 0:
            return ""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        __str__ method so that it returns [Rectangle] (<id>)
        <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x,
                self.__y, self.__width, self.__height
            )

    def update(self, *args, **kwargs):
        """
        Public method that assigns an argument to each attribute
        """
        if args:
            self = self.__dict__
            try:
                i = 0
                for k in self.keys():
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
        return self
