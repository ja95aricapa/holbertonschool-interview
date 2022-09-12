#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    newlist = []
    num = len(matrix)

    for i in range(num):
        newlist.append([])
        for j in range(num):
            newlist[i].append(matrix[j][i])

    matrix.clear()
    matrix += newlist
    for i in range(num):
        matrix[i].reverse()
