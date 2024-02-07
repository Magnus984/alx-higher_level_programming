#!/usr/bin/python3
"""Defines a function 'inherits_from'"""


def inherits_from(obj, a_class):
    """compares an object with a class.

    Returns:
        bool: True if object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise False.
    """
    if type(obj) is not a_class:
        return (issubclass(type(obj), a_class))
    return False
