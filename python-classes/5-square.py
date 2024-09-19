#!/usr/bin/python3
"""a square class"""


class Square:
    """Define a square with a given size."""

    def __init__(self, size =0):
        """Initialize the square with a given size."""
        self.__size = size

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
        """calbulate the area of square"""
        return self.__size**2

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print ()
        for row in range(self.size):
            print("#" * self.__size)
