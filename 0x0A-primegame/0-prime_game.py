#!/usr/bin/python3
"""A game with prime numbers"""


def is_prime(n):
    """Check if a number is a prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes_up_to(max_n):
    """Generate list of prime no.s up to max_n using Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]


def isWinner(x, nums):
    """
    Determine the winner of each game.
    :param x: Number of rounds
    :param nums: List of n values for each round
    :return: Name of the player that won the most rounds or None
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = generate_primes_up_to(max_n)
    prime_counts = [0] * (max_n + 1)

    # Precompute the number of primes up to each number
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1]
        if i in primes:
            prime_counts[i] += 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1  # Maria wins if the count of primes is odd
        else:
            ben_wins += 1  # Ben wins if the count of primes is even

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
