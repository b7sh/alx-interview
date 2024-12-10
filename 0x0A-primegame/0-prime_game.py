#!/usr/bin/python3
"""
a function isWineer - a solution to the Prime Game problem
"""


def primes(n):
    """
        Return list of prime numbers between 1 and n inclusive
        Arguments:
            n: integer
    """
    prime = []
    sieve = [True] * (n + 1)
    for pr in range(2, n + 1):
        if (sieve[pr]):
            prime.append(pr)
            for index in range(pr, n + 1, pr):
                sieve[index] = False
    return prime


def isWinner(x, nums):
    """
        Determines winner of Prime Game
    Args:
        x (int): rounds number
        nums (int): limit of rounds
    Return:
        a winner (Maria or Ben) or None
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for index in range(x):
        prime = primes(nums[index])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    return None
