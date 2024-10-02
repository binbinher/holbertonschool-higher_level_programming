#!/usr/bin/python3
"""a module contains a function save to json"""


import json

def save_to_json_file(my_obj, filename):
    """function that writes an Object to a JSON file"""
    with open(filename, "w", encoding="utf8") as my_file:
        json.dump(my_obj, my_file)
