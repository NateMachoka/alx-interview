#!/usr/bin/python3
"""
Function to rotate an n x n 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates the 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix (list of list of int): The n x n 2D matrix.
    """
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):  # Only swap above and including the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
