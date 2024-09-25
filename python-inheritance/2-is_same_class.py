#!/usr/bin/python3
"""a module that contains a function is_same_class"""

def is_same_class(obj, a_class):
    """
    function that return True if an object is
    exactly an instance of a specified class
    """
    return type(obj) is a_class
