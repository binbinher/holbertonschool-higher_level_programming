#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        return True
    else:
        return False

def uppercase(str):
    string = ""
    for char in str:
        if islower(char):
            string += chr(ord(char) - 32)
        else:
            string += char
    print("{:s}".format(string))
