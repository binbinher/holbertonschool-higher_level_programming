#!/usr/bin/python3
"""
a module contains a function from_json_string
"""


import json


def from_json_string(my_str):
    """
    function that returns a python data structure
    """
    return json.loads(my_str)
