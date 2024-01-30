#!/usr/bin/python3
"""
Defines a class rectangle.
"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initializes any object of rectangle class.

        Args:
            width(int): width of rectangle.
            height(int): height of rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Return the printable representation of the Rectangle.

        The rectangle is printed with the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """string representation of instance of rectangle"""
        rectangle = "Rectangle({}, {})".format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """Prints message when an instance of rectangle is deleted"""
        print("Bye rectangle...")

    @property
    def width(self):
        """gets width of instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width of a particular instance.

        Args:
            value(int): value to be used as width.
        Raises:
            TypeError: if value isn't an integer.
            ValueError: if value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height of a particular instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height of a particular instance.

        Args:
            value(int): value to be used as height.
        Raises:
            TypeError: if height(value) isn't an integer.
            ValueError: if height(value) is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))
