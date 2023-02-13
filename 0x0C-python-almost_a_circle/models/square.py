#!/usr/bin/python3
from models.rectangle import Rectangle
"""
class Square:
    Class that represents a Square and inherits from the Rectangle class.

    Attributes:
        size (int): size of the square.
        x (int): x coordinate of the square.
        y (int): y coordinate of the square.
        id (int): id of the square.
    """


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    """
    The __str__ method returns a string representation of the Square instance \
    in the specified format.
    """

    def __str__(self):

        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'
