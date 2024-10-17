#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    calculates the fewest number of operations needed,
    results in exactly n H characters in the file.
    """

    if not isinstance(n, int):
        return 0
    operations_count = 0
    current_copied = 0
    h_count = 1

    while h_count < n:
        if current_copied == 0:
            current_copied = h_count
            h_count += current_copied
            operations_count += 2

        elif n - h_count > 0 and (n - h_count) % h_count == 0:
            current_copied = h_count
            h_count += current_copied
            operations_count += 2

        elif current_copied > 0:
            h_count += current_copied
            operations_count += 1

    return operations_count
