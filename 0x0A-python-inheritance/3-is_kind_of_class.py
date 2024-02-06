#!/usr/bin/python3
"""Defines function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Compares an object and a class.

    Returns:
        bool: True if the object is an instance of, or if the
        object is an instance of a class that inherited from,
        the specified class; otherwise False.
    """
    return (isinstance(obj, a_class))
