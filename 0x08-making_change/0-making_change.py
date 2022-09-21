#!/usr/bin/python3
"""A Dynamic Programming based Python3 program to
    find minimum of coins to make a given change total"""
import sys


def makeChange(coins, total):

    if (total <= 0):
        return 0

    size = len(coins)

    table = [0 for i in range(total + 1)]

    table[0] = 0

    for i in range(1, total + 1):
        table[i] = sys.maxsize

    for i in range(1, total + 1):

        for j in range(size):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    if table[total] == sys.maxsize:
        return -1

    return table[total]
