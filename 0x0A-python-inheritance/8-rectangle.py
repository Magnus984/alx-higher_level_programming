#!/usr/bin/python3
"""Defines a class rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implements Rectangle class"""

    def __init__(self, width, height):
        """Initializes class rectangle.

        Args:
            width(int): width of rectangle.
            height(int): height of rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
