#!/usr/bin/python3
"""module defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Implements square class which inherits the rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes square class.

        Args:
            size(int): size of square object.
            x(int): x coordinate of square object.
            y(int): y coordinate of square object.
            id(int): object id.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width)
        return string

    @property
    def size(self):
        """Returns size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """sets size attribute.

        Args:
            value(int): size of square
        Raises:
            TypeError: if value is not an integer.
            ValueError: if size is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args and len(args) != 0:
            counter = 0
            for arg in args:
                if counter == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif counter == 1:
                    self.size = arg
                elif counter == 2:
                    self.x = arg
                elif counter == 3:
                    self.y = arg
                counter += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif key == "id":
                    self.id = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
