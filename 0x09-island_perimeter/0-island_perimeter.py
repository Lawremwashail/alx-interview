#!/usr/bin/python3
"""
    Island Perimeter function
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.
    Args:
        grid (list of list of int): A 2D grid representing the map.
    Returns:
        int: The perimeter of the island.
    """

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    edges = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 1

                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1

    return perimeter * 4 - edges * 2
