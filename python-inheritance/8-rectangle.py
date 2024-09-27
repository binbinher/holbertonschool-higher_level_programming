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
        """
        Initializes a Rectangle instance with width and height, 
        after validating that both are positive integers.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """

        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
