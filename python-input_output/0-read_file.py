#!/usr/bin/python3
"""a module contains a function that reads a text file"""


def read_file(filename=""):
    """function that opens a file"""
    with open(filename, encoding="utf-8") as my_file:
        for my_line in my_file:
            print(my_line, end="")
