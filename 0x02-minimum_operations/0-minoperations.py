#!/usr/bin/python3
"""
Module: 0-minoperations
Contains a function that calculates the minimum number of operations to
achieve exactly n 'H' characters in the text file using only Copy All and Paste.
"""

def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve n 'H'
    characters using only two operations: Copy All and Paste.

    Parameters:
        n (int): The target number of 'H' characters.
    Returns:
        int: The minimum number of operations required,
        or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Factorize n by dividing by smallest possible divisor
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
