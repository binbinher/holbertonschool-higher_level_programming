#!/usr/bin/python3
"""a module contains a function laod from json"""


import json


def load_from_json_file(filename):
    """a function that creates an Object from a JSON file"""
    with open(filename, "r", encoding="utf8") as my_file:
        return json.load(my_file)
