#!/usr/bin/python3


def minOperations(n):
    """
    Calculates the minimum number of operations required to reach a given number using the following operations:
     - Add 1
     - Multiply by 2

    Args:
        n (int): The target number.

    Returns:
        int: The minimum number of operations required to reach the target number.
    """
    if n <= 1:
        return 0

    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        if n % i == 0:
            operations[i] = i
            continue
        j = i - 1
        while j > 1:
            if i % j == 0:
                operations[i] = operations[j] + (i // j)
                break
            j -= 1

    return operations[n]
