#!/usr/bin/python3
"""A class Square"""


class Square:
    """Define a square with a given size"""

    def __init__(self, size=0):
        """instance attribute"""
        self.size = size

    @property
    def size(self):
        """Initialize the square with a given size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area of square"""
        return self.__size**2

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print()
        for row in range(self.size):
            print("#" * self.__size)
