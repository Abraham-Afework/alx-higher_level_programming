#!/usr/bin/python3
"""
This is the "Rectangle" module

Simple Rectangle class
"""


class Rectangle:
    """  Simple Rectangle Class with width and height attributs """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
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
        if(isinstance(self.print_symbol, str)):
            row = self.width * (self.print_symbol)
        else:
             row = self.width * repr(self.print_symbol)
        for h in range(self.__height):
            rectangle += str(row) + '\n'
        return rectangle[:-1]

    def __repr__(self):
        return "Rectangle({:d},{:d})".format(self.__width,self.__height)
            
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod      
    def bigger_or_equal(rect_1,rect_2):
        try:
            if not isinstance(rect_1,Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            if not isinstance(rect_2,Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle")
        except Exception as err:
                print(err)
                exit()
        else:
            if(rect_1.area() >= rect_2.area()):
                return rect_1
            else:
                return rect_2
    @classmethod
    def square(cls, size=0):
            return cls(size, size)