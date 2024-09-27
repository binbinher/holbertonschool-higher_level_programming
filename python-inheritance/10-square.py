#!/usr/bin/python3
"""defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square"""

    def __init__(self, size):
        """initialize a new square
        Args:
            size(int): the size of the new Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
