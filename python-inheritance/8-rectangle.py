#!/usr/bin/python3
"""
a class Rectangle which inherits from BaseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rectangle that inherits from BaseGeomety
    """

def __init__(self, width, height):
    self.width = width
    self.height =height
    self.integer_validator("height", height)
    self.integer_validator("width", width)
