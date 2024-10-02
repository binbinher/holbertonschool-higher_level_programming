#!/usr/bin/python3
"""
a module contains a class Student
"""


class Student:
    """class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialize a new student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retriveing a dictionary representating the student"""
        return self.__dict__
