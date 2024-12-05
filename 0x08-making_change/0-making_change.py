#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the dp table with a large number (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed for total 0

    # Loop through all coins
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, return -1 as it's impossible
    return dp[total] if dp[total] != float('inf') else -1
