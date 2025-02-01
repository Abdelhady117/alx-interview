#!/usr/bin/python3

""" Function to determine the winner of a game played x times
with the numbers in nums.
By Maria and Ben taking turns picking prime numbers from a list.
"""


def isWinner(x, nums):
    """
    Determines the winner of each game played optimally.
    """
    def sieve(n):
        """Returns a list where prime[i] is True if i is a prime number."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    if x < 1 or not nums:
        return None

    max_n = max(nums)
    prime_flags = sieve(max_n)
    prime_counts = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if prime_flags[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
