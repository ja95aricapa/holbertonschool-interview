#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file"""
    if n < 2 or type(n) is not int:
        return 0
    count = 1
    lists = list()
    value = n
    while value != 1:
        count += 1
        if value % count == 0:
            while value % count == 0 and value != 1:
                value /= count
                lists.append(count)

    return sum(lists)
