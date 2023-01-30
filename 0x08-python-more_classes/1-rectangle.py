#!/usr/bin/python3

class Rectangle:
            
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return  self.__width 
    
    @width.setter
    def width(self, value):
       
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
        return  self.__height 
    
    @height.setter
    def height(self, value):
       
        try:
            if not (isinstance(value, int)):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        except Exception as err:
            print(err)
    
