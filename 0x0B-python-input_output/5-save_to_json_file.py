#!/usr/bin/python3
"""Defines 'save_to_json_file' function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using a JSON represntation.

    Args:
        filename(str): name of file.
    """
    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write(json.dumps(my_obj))
