#!/usr/bin/python3
"""Defines a class Mylist"""


class MyList(list):
    """Inherits from list parent class"""

    def print_sorted(self):
        """Prints list, but in ascending order"""
        print(sorted(self))
