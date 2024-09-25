#!/usr/bin/python3
"""
a module contains Mylist class 
inherites from list
"""

class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
