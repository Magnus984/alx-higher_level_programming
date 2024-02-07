#!/usr/bin/python3
"""Define a 'load_from_json_file' function"""
import json


def load_from_json_file(filename):
    """Creates an object from a 'JSON file'

    Args:
        filename(str): name of file.
    """
    with open(filename, mode='r', encoding='utf-8') as myFile:
        return json.loads(myFile.read())
