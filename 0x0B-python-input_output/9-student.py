#!/usr/bin/python3
"""
A "class_Student" function container
"""


class Student:
    """Representation of a Student"""

    def __int__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        return self.__dict__
