from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        perimeter = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:  # Only process land cells
                    # Check all four sides:
                    # Top
                    if r == 0 or grid[r-1][c] == 0:
                        perimeter += 1
                    # Bottom
                    if r == ROWS-1 or grid[r+1][c] == 0:
                        perimeter += 1
                    # Left
                    if c == 0 or grid[r][c-1] == 0:
                        perimeter += 1
                    # Right
                    if c == COLS-1 or grid[r][c+1] == 0:
                        perimeter += 1

        return perimeter
