#!/usr/bin/python3
"""Defines a function which prints a square"""


def print_square(size):
    """prints # size number of times in a square

    Args:
        size(int): size of square.
    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is lesser than zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
    if size == 0:
        print()
