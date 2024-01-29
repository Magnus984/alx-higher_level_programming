#!/usr/bin/python3
"""
Defines a class rectangle
"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initializes any object of rectangle class.

        Args:
            width(int): width of rectangle.
            height(int): height of rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets width of instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width of a particular instance.

        Args:
            value(int): value to be used as width.
        Raises:
            TypeError: if value isn't an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height of a particular instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height of a particular instance.

        Args:
            value(int): value to be used as height.
        Raises:
            TypeError: if height(value) isn't an integer.
            ValueError: if height(value) is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
