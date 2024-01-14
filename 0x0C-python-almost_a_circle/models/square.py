#!/usr/bin/pythonv3
"""
Class Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defining the class Square that inherits from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the superclass constructor with id, x, y, width, and height
        """
        super().__init__(size, size, x, y, id)

    """
    Override the __str__ method
    """
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    """
    Override the update method to allow updating
    size using key-worded arguments
    """
    def update(self, *args, **kwargs):
        if args:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    """
    Public method to return dictionary representation
    """
    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    """
    Public getter and Setter for size
    """
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.__validate_positive_int("width", value)
        self.width = value
        self.height = value

    """
    Validating positive integers with private helper method
    """
    def __validate_positive_int(self, attr_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{attr_name} must be > 0")
