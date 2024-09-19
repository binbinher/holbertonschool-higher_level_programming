#!/usr/bin/python3
"""a square class"""


class Square:
    """define a square with given size"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize the square with a give size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self, value):
        """"set the position of the square"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) and num >= 0 for num in value)
				):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate the area of the square"""
        return self.__size**2

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
