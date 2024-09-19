#!/usr/bin/python3
"""A class Square"""


class Square:
    """A Square class that devine a square"""
    
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """private instance attribute"""
        self.__size = size
        