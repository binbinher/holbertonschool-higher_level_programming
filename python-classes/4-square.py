#!/usr/bin/python3
"""a class square"""


class Square:
    """a square class that defind a square"""

    def __init__(self, size=0):
        """instance attribute"""
        self.size = size

    @property
    def size(self):
        """get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate area of square"""
        return self.__size**2
