#!/usr/bin/python3
"""
a module contains a function class_to_json
"""


def class_to_json(obj):
    """
    a function that returns the dictionary with date structure
    """
    return obj.__dict__
