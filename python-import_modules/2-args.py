#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numofArgs = len(argv)
    if numofArgs - 1 == 0:
        print("{} arguments.\n".format(numofArgs - 1), end="")
    elif numofArgs - 1 == 1:
        print("{} argument:\n".format(numofArgs - 1), end="")
    else:
        print("{} arguments:\n".format(numofArgs - 1), end="")

    if numofArgs != 0:
        for index in range(1, numofArgs):
            print("{}: {}".format(index, argv[index]))
