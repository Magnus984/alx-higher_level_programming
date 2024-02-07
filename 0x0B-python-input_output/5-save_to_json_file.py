#!/usr/bin/python3
import json
"""Defines 'save_to_json_file' function"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using a JSON represntation.

    Args:
        filename(str): name of file.
    """
    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write(json.dumps(my_obj))
