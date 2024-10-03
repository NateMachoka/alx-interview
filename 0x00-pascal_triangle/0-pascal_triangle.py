#!/usr/bin/python3
"""
A function to generate Pascal's triangle up to the nth row.
The triangle is represented as a list of lists of integers.
"""


def pascal_triangle(n):
    """Creates Pascal's triangle upto the `n`th level

        Args:
            n (number): The number of levels to show
        Returns:
            A list of lists of integers representing Pascal's triangle
            [] otherwise
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start a new row with '1'
        row = [1] * (i + 1)

        # Each triangle row has values that are the sum of the two values above
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
