#!/usr/bin/python3
""" Class Module"""


class Base:
    """
    Base class
    Private class attribute:
        __nb_object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        args:
            id: id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
