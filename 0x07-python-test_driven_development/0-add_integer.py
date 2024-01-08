#!/usr/bin/python3
"""Defines integer addition function."""


def add_integer(a, b=98):
    """
    addition of integer: a and b.

    Returns: addition of two integers.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        newfig_a, newfig_b = int(a), int(b)
        return newfig_a + newfig_b
