#!/usr/bin/python3
"""Module which defines Base class."""


class Base():
    """Implements Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class.

        Args:
            id(int): class id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
