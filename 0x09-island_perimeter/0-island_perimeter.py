#!/usr/bin/python3
"""
Module to calculate the perimeter of an island described in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    Args:
        grid (list of list of int): The grid representing the island, where
                                    0 represents water and 1 represents land.
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 sides for each land cell
                perimeter += 4
                # Subtract 2 for each horizontal neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                # Subtract 2 for each vertical neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
