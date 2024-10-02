#!/usr/bin/python3
"""
a module contains a class Student
"""


class Student:
    """a class defines a student"""
    def __init__(self, first_name, last_name, age):
        """initializing a new student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.aqe = age

    def to_json(self, attrs=None):
        """retriving a dictionary representing the student"""
        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: self.__dict__[attr]
                for attr in attrs if attr in self.__dict__
            }
  