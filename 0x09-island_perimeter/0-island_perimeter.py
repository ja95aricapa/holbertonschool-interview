#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """function that returns the perimeter
    of the island described in grid
    """
    perimeter = 0
    base = len(grid)
    height = len(grid[0]) if base else 0

    for b in range(len(grid)):
        for h in range(len(grid[b])):
            index = [(b - 1, h), (b, h - 1), (b, h + 1), (b + 1, h)]
            check = [
                1 if k[0] in range(base) and k[1] in range(height) else 0
                for k in index
                ]

            if grid[b][h]:
                perimeter += sum([
                    1 if not r or not grid[k[0]][k[1]] else 0
                    for r, k in zip(check, index)
                    ])

    return (perimeter)
