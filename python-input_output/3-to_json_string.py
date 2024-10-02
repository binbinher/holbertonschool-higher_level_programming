#!/usr/bin/python3
"""a module contains a function returns the JSON"""

import json


def to_json_string(my_obj):
    """a function return the JSON representation of an object"""
    return json.dumps(my_obj)
