#!/usr/bin/python3
"""
a module contains an inherited class-checking function.
"""


def inherits_from(obj, a_class):
    """
    checks if an object is an inherited instance of a class.

    Arg:
        obj(any): The object to check.
        a_class(tpye): the class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class -True.
        Otherwise -False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
