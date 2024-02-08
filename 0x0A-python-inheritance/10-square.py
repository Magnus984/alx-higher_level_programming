#!/usr/bin/python3
"""Defines a square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Implements a class rectangle"""

    def __init__(self, size):
        """Initializes class.

        Args:
            size(int): size of square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Computes area of square"""
        return self.__size * self.__size
