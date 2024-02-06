#!/usr/bin/python3
"""Defines a function that lists attributes of an object"""


def lookup(obj):
    """Returns the list of attributes and methods of an object.

    Args:
        obj: object.
    """

    return dir(obj)
