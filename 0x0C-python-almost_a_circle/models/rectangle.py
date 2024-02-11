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
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return __x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return

    @y.setter
    def y(self, value):
        self.__y = value
