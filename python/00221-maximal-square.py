from typing import List

def maximalSquare(matrix: List[List[str]]) -> int:
    # Get the number of rows and columns in the matrix
    ROWS, COLS = len(matrix), len(matrix[0])

    # Create a cache to store the maximum side length of the square
    cache = {}  # Map each (r, c) -> maxLength of square

    def helper(r, c):
        if r >= ROWS or c >= COLS:
            return 0

        if (r, c) not in cache:
            down = helper(r + 1, c)
            right = helper(r, c + 1)
            diag = helper(r + 1, c + 1)

            cache[(r, c)] = 0

            if matrix[r][c] == "1":
                cache[(r, c)] = 1 + min(down, right, diag)

        return cache[(r, c)]

    helper(0, 0)
    return max(cache.values()) ** 2
