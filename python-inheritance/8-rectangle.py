#!/usr/bin/python3
"""
a class Rectangle which inherits from BaseGeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeomety
    This class represents a rectangle and validates its width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height, 
        after validating that both are positive integers.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
