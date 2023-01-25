#!/usr/bin/python3
""" Define a class Square """


class Square:

    """ defines a method called __init__"""
    def __init__(self, size=0):

        """ if statement"""

        if not isinstance(size, int):

            """ raise error"""
            raise TypeError("size must be an integer")

        elif size < 0:
            """ raise Error"""

            raise ValueError("size must be >= 0")

        else:

            """ initialize private _size of self with size """
            self.__size = size

        def area(self):
            """ return the area of a square"""
            return self.__size ** 2
