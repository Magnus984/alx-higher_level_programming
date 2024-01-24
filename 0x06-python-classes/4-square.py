#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new square instance.

        Args:
            size(int):size of square
        """
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the current size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
