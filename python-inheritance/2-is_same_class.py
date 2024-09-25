#!/usr/bin/python3
"""a module that contains a function that returns True
if the object is exactly an instance of the specified class"""

def is_same_class(obj, a_class):
    """
    fucntion return True or false to check 
    the object is an instance of a specified class or not
    """
    return type(obj) is a_class
