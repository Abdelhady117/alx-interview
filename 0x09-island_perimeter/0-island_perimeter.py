#!/usr/bin/python3
"""
Create a function that returns the perimeter of the island described in grid:
grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Start with 4 sides
                perimeter += 4
                # Check for adjacent land cells and subtract shared sides
                if r > 0 and grid[r-1][c] == 1:  # Check above
                    perimeter -= 2
                if c > 0 and grid[r][c-1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
