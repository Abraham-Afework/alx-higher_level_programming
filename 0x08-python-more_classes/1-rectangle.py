#!/usr/bin/python3
""" Define the Rectangle class """


class Rectangle:
    """ Rectangle Class """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """ Initialize a new Rectangle.

        Args:
            width(int): The width of the new Rectangle
            height(int): The height of the Rectangle
    """
    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
