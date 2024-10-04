#!/usr/bin/python3
"""
this basic serialization module contains functions 
to serialize a python dic to json file and 
deserilize the JSON file to recreate the python dic
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    funciton that adds the functionality to serialize a Python dictionary 
    
    Args:
        data(dict): A Python Dictionary with data
        filename(str): The filename of the output JSON file. 
        If the output file already exists it should be replaced.
    """
    with open(filename, "w")as my_file:
        json.dump(data, my_file)


def load_and_deserialize(filename):
    """
    funciton that deserialize the JSON file to recreate the Python Dictionary.
    
    Args:
        filename(str): The filename of the input JSON file. 
    Returns:
        a python dictionary with deserialized JSON data
    """
    with open(filename, "r") as my_file:
        return json.load(my_file)
