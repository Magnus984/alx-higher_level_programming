#!/usr/bin/python3
"""Module defines Rectanlge class"""
from models.base import Base


class Rectangle(Base):
    """Implements Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle class.

        Args:
            width(int): width
            height(int): height
            x(int): x
            y(int): y
        Raises:
            TypeError: if input is not an integer
            ValueError: if width or height is under or equals 0.
            Also if x or y is under 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """sets x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """sets y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area value of a rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for y in range(self.y):
            print("")
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end='')
            print("")

    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width) + "/" + str(self.height)
        return string

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            counter = 0
            for arg in args:
                if counter == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif counter == 1:
                    self.width = arg
                elif counter == 2:
                    self.height = arg
                elif counter == 3:
                    self.x = arg
                elif counter == 4:
                    self.y = arg
                counter += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                elif key == "id":
                    self.id = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """retuns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
