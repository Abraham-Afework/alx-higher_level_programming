#!/usr/bin/python3
"""" Defines a Square class   """
from models.rectangle import Rectangle
"""
class Square:
    Class that represents a Square and inherits from the Rectangle class.
"""


class Square(Rectangle):
    """
        Represents a Square

    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes a new square with

        Attributes:
                        size (int): size of the square.
                        x (int): x coordinate of the square.
                        y (int): y coordinate of the square.
                        id (int): identity of the square.
        """
        self.size = size
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    """
    The __str__ method returns a string representation of the Square instance \
    in the specified format.
    """

    def __str__(self):
        """ Returns the string representation of a Square """

        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    
    @property
    def size(self):
        """  getter method for the square size """
        return self.width

    
    @size.setter
    def size(self, value):
        """ setter method for a square size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ method that updates the suare attributs

            *args is the list of arguments - no-keyworded arguments
                            1st argument should be the id attribute
                            2nd argument should be the size attribute
                            3rd argument should be the x attribute
                            4th argument should be the y attribute
            **kwargs:
            key word arrgument representing the following attributes
                - id
                - size
                - x
                - y
            **kwargs will be skipped if *args exists and is not empty
        """
        if len(args) > 0:
            try:
                args[0]
                self.id = args[0]
                args[1]
                self.size = args[1]
                args[2]
                self.x = args[2]
                args[3]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        square_dictionary = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'size': self.height
        }
        return square_dictionary
