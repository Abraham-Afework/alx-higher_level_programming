#!/usr/bin/python3
"""
This is the "Rectangle" module

Simple Rectangle class
"""


class Rectangle:
    """  Simple Rectangle Class with width and height attributs """
    number_of_instances = 0
    print_symbol = "#"

    """ Initialize a new Rectangle. """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """ area of the rectangle
        :return: the area of the area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ perimeter of the rectangle
        :return: the perimeter of the area
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height*2)

    def __str__(self):

        rectangle = ""
        if type(self.print_symbol) == str:
            row = self.width * self.print_symbol
        else:
            row = self.width * repr(self.print_symbol)
        for h in range(self.__height):
            rectangle += str(row) + '\n'
        return rectangle[:-1]

    def __repr__(self):
        """ string representation of the \\
        rectangle to be able to recreate a new instance \\
        :return: the string representation
        """
        return "Rectangle({:d},{:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        prints bye rectangle when an instance of a class is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1,  rect_2):
        """Compares and two rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if (rect_1.area() >= rect_2.area()):
                return rect_1
            else:
                return rect_2

    """ class method declaration """
    @classmethod
    def square(cls, size=0):
        """ square class
            return: width and height equal to size
        """
        return (cls(size, size))
