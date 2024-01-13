#!/usr/bin/python3
"""
Class Module
"""
from models.base import Base


class Rectangle(Base):
    """
    Defining the class Rectangle that inherits from class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Call the superclass constructor with id
        """
        super().__init__(id)

        """
        We assign each argument to the right attribute
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """
    The getter and setter for width
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_positive_int("width", value)
        self.__width = value

    """
    The getter and setter for height
    """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_positive_int("height", value)
        self.__height = value

    """
    The getter and setter for x
    """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__validate_non_negative_int("x", value)
        self.__x = value

    """
    The getter and setter for y
    """
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__validate_non_negative_int("y", value)
        self.__y = value

    """
    Public method to calculate and return the area
    """
    def area(self):
        return self.width * self.height

    """
    Improved public method to display the rectangle using '#'
    """
    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    """
    Override the __str__ method
    """
    def __str__(self):
        return (f"[Rectangle] ({self.id}) "
                f"({self.x}/{self.y} - {self.width}/{self.height})")

    """
    Public method to return dictionary representation
    """
    def to_dictionary(self):
        return{'id': self.id, 'width': self.width,
               'height': self.height, 'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        if args:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    """
    Validating positive integers with private helper method
    """
    def __validate_positive_int(self, attr_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    """
    Validating non-negative integers with private helper method
    """
    def __validate_non_negative_int(self, attr_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        elif value < 0:
            raise ValueError(f"{attr_name} must be >= 0")
