#!/usr/bin/python3
"""Function to calculate the amount of rainwater retained between walls."""


def rain(walls):
    """Calculate the amount of rainwater retained between walls.

    Args:
        walls (List[int]): A list of non-negative integers.

    Returns:
        int: The total amount of rainwater retained.

    Example:
        >>> rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        6

    """

    left = 0
    right = len(walls) - 1
    left_max = 0
    right_max = 0
    total_water = 0

    while left < right:
        if walls[left] <= walls[right]:
            if walls[left] > left_max:
                left_max = walls[left]
            else:
                total_water += left_max - walls[left]
            left += 1
        else:
            if walls[right] > right_max:
                right_max = walls[right]
            else:
                total_water += right_max - walls[right]
            right -= 1

    return total_water
