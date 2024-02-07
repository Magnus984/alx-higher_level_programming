#!/usr/bin/python3
"""Defines 'append_write' function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file(UTF8)
    and returns the number of characters added

    Args:
        filename(str): name of file.
        text(str): string to append to file.
    """
    with open(filename, mode='a', encoding='utf-8') as myFile:
        return myFile.write(text)
