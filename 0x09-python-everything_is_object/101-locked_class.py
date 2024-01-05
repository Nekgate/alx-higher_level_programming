#!/usr/bin/python3


class LockedClass:
    """ Locked class: We can't set instance attribute to it"""
    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
