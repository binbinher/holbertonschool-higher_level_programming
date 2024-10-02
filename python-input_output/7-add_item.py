#!/usr/bin/python3
"""a module that contains a script that adds all arguments to a python list"""


import sys
import os
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

# load existing iteams if the file exisits, otherwise start with an empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# all all arguments to the list
items.extend(sys.argv[1:])

#save the updated list back to the file
save_to_json_file(items, filename)
