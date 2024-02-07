#!/usr/bin/python3
"""Defines 'read_file' function"""


def read_file(filename=""):
    """Reads a text file(UTF8) and prints it to stdout.

    Args:
        filename(str): name of file.
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
