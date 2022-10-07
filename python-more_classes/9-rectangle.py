#!/usr/bin/python3
"""
A rectangle with width and height.
"""


class Rectangle:
    """
    Rectangle functions and data
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width
        """
        return self.__width

    @property
    def height(self):
        """getter for height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """setter for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for width
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Standard method that prints the rectangle with character #
        """
        strr = ""
        if self.__width == 0 or self.__height == 0:
            return strr

        for i in range(self.__height):
            if i == self.__height - 1:
                strr += (str(self.print_symbol) * self.__width)
            else:
                strr += ((str(self.print_symbol) * self.__width) + '\n')
        return strr

    def __repr__(self):
        """Returns a String with a representation
        of the state of the object"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a strr when object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """"Static method that returns the biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
