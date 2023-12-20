#!/usr/bin/python3
# 3-Square.py based on 2-square.py
"""Defines a Square module """


class Square:
    """ Represents a square class """

    def __init__(self, size=0) -> None:
        """
        Intializes class attributes

        Args:
            size: size of square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of a square
        """
        return self.__size ** 2
