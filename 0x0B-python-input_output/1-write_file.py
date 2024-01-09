#!/usr/bin/python3
"""The write_file function container"""


def read_file(filename="", text=""):
    """""write_file, This writes a string to text file.
    Args:
        filename (str): Name of file.
        text (str): Text to be written.
        Return: The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        files = file.write()
        return (files)
