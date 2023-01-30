#!/usr/bin/python3
""" Define the Rectangle class """


class Rectangle:
    """ Rectangle Class """
    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle.

        Args:
            width(int): The width of the new Rectangle
            height(int): The height of the Rectangle
         """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        try:
            if not (isinstance(value, int)):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        except Exception as err:
            print(err)

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height of the rectangle """
        try:
            if not (isinstance(value, int)):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        except Exception as err:
            print(err)

    def area(self):
        """ area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height*2)

    def __str__(self):
        """prints in stdout the area with the character # """
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle
        else:
            row = self.width * "#"
            for h in range(self.__height):
                rectangle += row + '\n'
            return rectangle[:-1]

    def __repr__(self):
        """
        string representation of the rectangle
        to be able to recreate a new instance
        :return: the string representation
        """
        return "Rectangle({:d},{:d})".format(self.__width, self.__height)
