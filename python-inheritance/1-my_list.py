#!/usr/bin/python3
"""
This module contains a MyList class that inherits from list.
"""

class MyList(list):
    """
    A class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in a sorted order (ascending).
        """
        print(sorted(self))
