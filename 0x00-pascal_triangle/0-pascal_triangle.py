#!/usr/bin/python3
"""
pascal's triangle
"""


def pascal_triangle(n):
    """
    checks if trinagle is empty
    returns an empty list if n is empty
    intitializes empty triangle list
    """
    triangle = []

    if n <= 0:
        return triangle

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(len(triangle[i - 1]) - 1):
            current_row = triangle[i - 1]
            row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        row.append(1)
        triangle.append(row)
    return triangle
