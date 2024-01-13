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
            args = args[1:]

        if args:
            self.size = args[0]
        elif 'size' in kwargs:
            self.size = kwargs['size']

    """
    Getter and Setter for size
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
