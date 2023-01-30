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

    def area(self):

        return (self.__width * self.__height)
    
    def perimeter(self):
        
        if self.__width == 0 or self.__height == 0:
            
            return 0
        else:
            
            return (self.__width * 2) + (self.__height*2)
    def __str__(self):
        rectangle = ""
        row = self.width * "#"
        for h in range(self.__height):
            rectangle += row + '\n'
        return rectangle[:-1]
    def __repr__(self):
        return "Rectangle({:d},{:d})".format(self.__width,self.__height)
