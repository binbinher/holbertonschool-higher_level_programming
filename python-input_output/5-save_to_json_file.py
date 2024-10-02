#!/usr/bin/python3
"""
a module contains a function to save an object to json file
"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a JSON file
    args:
    my_obj: the object to serialize and write to a file
    filename(str): the name of the file to save the JSON data.
    """
    with open(filename, "w", encoding="utf8") as my_file:
        json.dump(my_obj, my_file)
