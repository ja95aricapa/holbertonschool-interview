#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(number):
    """
    Create a list of numbers for the pascal triange
    """
    triangle = []
    row = []
    prev_row = []
    for i in range(0, number + 1):
        row = [
            j > 0 and j < i - 1 and i > 2 and
            prev_row[j-1] + prev_row[j] or 1 for j in range(0, i)
        ]
        prev_row = row
        triangle += [row]
    if number > 0:
        return triangle[1:]
    else:
        triangle = []
        return triangle
