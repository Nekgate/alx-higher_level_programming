#!/usr/bin/python3
"""A class Square that inherits from Rectangle (9-rectangle.py)
(task based on 10-sqare.py"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class."""
    def __init__(self, size):
        """Initialize a new square.
        """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return("[Square] " + str(self.__size) + "/" + str(self.__size))
