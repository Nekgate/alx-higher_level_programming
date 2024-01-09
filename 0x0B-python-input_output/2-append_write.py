#!/usr/bin/python3
"""A function that appends a string"""


def append_write(filename="", text=""):
    """appends a string at the end of textfile and returns character"""
    with open(filename, "a", encoding="utf-8") as file:
        lines = file.write(text)
        return lines
