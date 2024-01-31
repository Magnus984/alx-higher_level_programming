#!/usr/bin/python3
"""Defines a function that adds numbers"""


def add_integer(a, b=98):
    """Returns the addition of a and b

    Args:
        a(int): first number
        b(int): second number
    Raises:
        TypeError: if either a or b is not a number
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
