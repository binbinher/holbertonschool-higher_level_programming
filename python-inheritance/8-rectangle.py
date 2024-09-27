#!/usr/bin/python3
"""
a class Rectangle which inherits from BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeomety
    """

def __init__(self, width, height):
    self.__width = width
    self.__height = height
    self.integer_validator("height", height)
    self.integer_validator("width", width)
