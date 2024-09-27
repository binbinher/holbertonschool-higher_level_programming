#！/usr/bin/python3

from abc import ABC

class Animal(ABC):
    """an abstract class Animal"""

    @abstractmethod
    def sound(self):
        """"Abstract method sound"""
        pass

class Dog(Animal):
    """class Dog inherits from Animal class"""

    def sound(self):
        """abstract method sound"""
        return "Bark"

class Cat(Animal):
    """class Cat inherits from Animal class"""

    def sound(self):
        """abstract method sound"""
        return "Meow"
