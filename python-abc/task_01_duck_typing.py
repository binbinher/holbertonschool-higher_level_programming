#!/usr/bin/python3

from abc import ABC, abstractmethod
import math

"""a class Shape and 2 subclass circle and rectangle"""

class Shape(ABC):
    """an abstract class Shape"""
    @abstractmethod
    def area(self):
        """abstract method area"""
        pass

    @abstractmethod
    def perimeter(self):
        """abstract method perimeter"""
        pass

    class Circle(Shape):
        """class Circle inherits from Shape"""
        def __init__(self, radius):
            """circle constructor"""
            self.radius = abs(radius)

        def area(self):
            """area method cirble"""
            return math.pi * self.radius**2

        def perimeter(self):
            """perimeter method circle"""
            return math.pi * 2 * self.radius

    class Rectangle(Shape):
        """class Rectangle inherits from Shape"""
        def __init__(self, width, height):
            """Rectangle constructor"""
            self.width = width
            self.height = height 

        def area(self):
            """area method rectangle"""
            return self.width * self.height

        def perimeter(self):
            """perimeter method rectangle"""
            return 2 * (self.width + self.height)

        def shape_info(shape):
            """a function that takes a single arugument"""
            print("Area:", shape.area())
            print("Perimeter:", shape.perimeter())
