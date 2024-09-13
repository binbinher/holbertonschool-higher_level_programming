#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    for number in my_list:
        unique.add(number)
    return sum(unique)
