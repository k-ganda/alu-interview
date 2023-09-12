#!/usr/bin/python3
"""
Method to calculate minimum number of
operations required to reach a given number
"""


def minOperations(n):
    """Calculation  of operations needed to obtain exactly n H characters

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations required.
    """

    if n <= 1:
        return 0

    operations = 0
    i = 2
    while i <= n:
        if n % i == 0:
            operations += i
            n //= i
        else:
            i += 1

    return operations
