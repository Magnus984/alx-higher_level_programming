#!/usr/bin/python3
"""Module which defines Base class."""
import json


class Base():
    """Implements Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class.

        Args:
            id(int): class id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries.

        Args:
            list_dictionaries(dict): a list of dictionaries.
        """
        if list_dictionaries and len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON string representation of
        list_objs to a file.

        Args:
            list_objs(obj): list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding="utf-8") as myFile:
            if list_objs is None:
                myFile.write([""])
            else:
                listDict = [obj.to_dictionary() for obj in list_objs]
                json_string = Base.to_json_string(listDict)
                myFile.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation json_string.

        Args:
            json_string(str): a string representing a list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.

        Args:
            dictionary(dict): can be thought of as double pointer
            to a dictionary
        """
        if cls.__name__ == "Rectangle":
            some_object = cls(6, 5)
        else:
            some_object = cls(6)
        some_object.update(**dictionary)
        return some_object

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as myFile:
                listDict = Base.from_json_string(myFile.read())
                return [cls.create(**dic) for dic in listDict]
        except IOError:
            return []
