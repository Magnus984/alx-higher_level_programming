#!/usr/bin/python3
import json
"""Define a 'load_from_json_file' function"""


def load_from_json_file(filename):
    """Creates an object from a 'JSON file'

    Args:
        filename(str): name of file.
    """
    with open(filename, mode='r', encoding='utf-8') as myFile:
       return json.loads(myFile.read())
