#!/usr/bin/python3
"""Defines function 'from_json_string'"""
import json


def from_json_string(my_str):
    """Returns an object(Python data structure) represented
    by a JSON string
    
    Args:
        my_str(str): string to be deserialized.
    """
    return json.loads(my_str)
