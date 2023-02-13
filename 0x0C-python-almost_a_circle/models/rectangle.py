#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that represents a rectangle shape in two-dimensional space
    Inherits from Base class and provides additional properties and methods\
    for working rectanglee
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
        - width (int): the width of the rectangle.\
                Must be an intger greater than 0.
        - height (int): the height of the rectangle .\
                Must be an intger and greater than 0.
        - x (int, optional): the x-coordinate of a rectangle.\
                Must be an integer greater than or equal to 0. Default is 0.
        - y (int, optional): the y-coordinate of a rectangle. \
                Must be an integer greater than or equal to 0. Default is 0.
        - id (int or None, optional): the identifer of the rectangle.\
                Default is None

        Raises:
        -TypeError: if width, height, x, or y is not an integer
        -ValueError: if width or height is less than or equal to 0,\
                :or if x or y is less than 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        The width of the rectangle.

        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            int value: the new width of the rectangle.\
                    Must be an integer greater than 0.
        Raises:
            TypeError: if value is not intger
            ValueError: if value is less than or equal to 0
        """

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        The height of the rectangle.

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            int value: the new height of the rectangle.\
                    Must be an integer greater than 0.
        Raises:
                TypeError: if value is not intger
                ValueError: if value is less than or equal to 0

                """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        The x- coordinate of a rectangle

        Returns:
                int: the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """

                Sets the x- coordinates of the rectangle.

                Args:
                int value: the new x coordinates of the rectangle.\
                 Must be an integer greater than or equal to 0.

                Raises:
                TypeError: if value is not intger
                ValueError: if value is less than 0

                """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
                The y-coordinate of a rectangle

                Returns:
                int: the value of y
                """
        return self.__y

    @y.setter
    def y(self, value):
        """

                Sets the y- coordinates of the rectangle.

                Args:
                int value: the new y coordinates of the rectangle.\
                 Must be an integer greater than or equal to 0.

                Raises:
                TypeError: if value is not intger
                ValueError: if value is less than 0

                """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
                Method that returns the area of a rectangle

                """
        return self.__width * self.__height

    def display(self):
        """
                Method that prints stdout Rectangle with a character #

                """
        string = "\n" * self.__y
        for h in range(self.__height):
            character = " " * self.__x
            for w in range(self.__width):
                character += "#"
            string += character + "\n"
        print(string, end="")

    def __str__(self):
        """
        Method that returns a string representation of a rectangle object

        Returns:
                str: [Rectangle] (id) x/y - width/height
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Method that updates the attribute of an object

        Args:
            *args:
                - 1st argument is id attribute
                - 2nd argument is width attribute
                - 3rd argument is height attribute
                - 4th argument is x attribute
                - 5th argument is y attribute

            **kwargs:
                key word arrgument representing the following attributes
                    - id
                    - width
                    - height
                    - x
                    - y
            If '*args' is passed, its values will be assigned to the \
            corresponding attributes in the order specified above.

            If '**kwargs' is passed, its values will be assigned to the \
            attributes with matching keys.

            If both '*args' and '**kwargs' are passed,\
            the values in **kwargs will be ignored.

        """
        if len(args) > 0:
            try:
                args[0]
                self.id = args[0]
                args[1]
                self.__width = args[1]
                args[2]
                self.__height = args[2]
                args[3]
                self.__x = args[3]
                args[4]
                self.__y = args[4]

            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle"""
        rectangle_dictionary = {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
        }
        return rectangle_dictionary
