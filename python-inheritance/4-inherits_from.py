#!/usr/bin/python3
"""
a module contains a function that return true or false
if the object if an instance of a class that inheried from the class
"""

def inherits_from(obj, a_class):
    """
    a function that returns True if the object 
    is an instance of a class that inherited 
    from the specified class ; otherwise False.
    """
    return type(obj) is not a_class and isinstance(ojb, a_class)
