#!/usr/bin/python3

from abc import ABC, abstractmethod
import math

"""a class Shape and 2 subclass circle and rectangle"""

class Shape(ABC):
    """An abstract class Shape"""
    
    @abstractmethod
    def area(self):
        """Abstract method to calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter"""
        pass


class Circle(Shape):
    """Class Circle inherits from Shape"""
    
    def __init__(self, radius):
        """Circle constructor"""
        self.radius = abs(radius)

    def area(self):
        """Calculate the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class Rectangle inherits from Shape"""
    
    def __init__(self, width, height):
        """Rectangle constructor"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """A function that takes a Shape object and prints its area and perimeter"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
