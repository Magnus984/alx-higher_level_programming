#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry():
    """Implements a BaseGeometry class"""

    def area(self):
        """Area not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
            name(str): string to validate
            value(int): number to validate
        Raises:
        TypeError: if value is not an integer.
        ValueError: if value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
