#!/usr/bin/python3
"""
module that contain a function that returns 
a list of availalbe attributes and methods of an object
"""


def lookup(obj):
    """
    function that returns a list of available
    attributes and methods of an object
    """
    return dir(obj)
