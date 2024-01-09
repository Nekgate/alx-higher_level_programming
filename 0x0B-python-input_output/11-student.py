#!/usr/bin/python3
"""
Module for Student class.
"""


class Student:
    """Class for jsonification."""
    def __int__(self, first_name, last_name, age):
        """Constructor."""
        self.first_name = first_name
        self.first_name = last_name
        self.age = age

    def to_json(self, attrbs=None):
        """Retrieves dictionary with filter."""
        if type(attrbs) is list and ([type(x) == str for x in attrbs]):
            return {k: v for k, v in self.__dict__.items() if k in attrbs}
        else:
            return self.__dict__.copy()

    def reload_from_jason(self, json):
        """Loads attributes from json."""
        for key, value in json.items():
            self.__dict__[key] = value
