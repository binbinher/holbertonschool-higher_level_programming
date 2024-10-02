#!/usr/bin/python3
"""a module contains a function pascal_triangle"""


def pascal_triangle(n):
    """a function that returns a list of lists of integers"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1,n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
