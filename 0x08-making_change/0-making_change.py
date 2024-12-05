#!/usr/bin/python3
"""
Module to calculate the minimum number of coins needed to make a given amount.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    Args:
        coins (list): A list of integers representing coin denominations.
        total (int): The total amount to be made.
    Returns:
        int: The fewest number of coins needed, -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize the dp array with a very large value (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make 0 amount

    # Fill the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means total can't be formed
    return dp[total] if dp[total] != float('inf') else -1
