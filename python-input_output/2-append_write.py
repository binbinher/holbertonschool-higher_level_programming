#!/usr/bin/python3
"""a module contains a function append_write"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8)"""
    with open(filename, "a", encoding="utf8")as my_file:
        return my_file.write(text)
