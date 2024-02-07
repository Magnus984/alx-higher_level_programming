#!/usr/bin/python3
"""Defines 'write_file' function"""


def write_file(filename="", text=""):
    """writes a string to a text file(UTF8) and returns the number
    of characters written

    Args:
        filename(str): name of file.
        text(str): string to write to file.
    """
    with open(filename, mode='w', encoding='utf-8') as myFile:
        return myFile.write(text)
