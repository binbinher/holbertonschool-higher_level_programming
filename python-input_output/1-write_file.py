#!/usr/bin/python3
"""a module contains a function that writes a string"""


def write_file(filename="", text=""):
    """a function  that writes a string to a text file"""
    with open(filename, "w", encoding="utf8") as my_file:
        return my_file.write(text)
