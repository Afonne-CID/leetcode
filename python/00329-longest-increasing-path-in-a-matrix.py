def longestIncreasingPath(matrix):
    # Dimensions of the matrix
    ROWS, COLS = len(matrix), len(matrix[0])

    # Cache to store computed results (row, col) -> Longest Increasing Path (LIP)
    dp = {}

    def dfs(r, c, prevVal):
        # Check if we are out of bounds or if the path is not increasing
        if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
            return 0

        # Check if we have already computed the LIP for this position
        if (r, c) in dp:
            return dp[(r, c)]

        # Initialize the result with 1 (the minimum path length)
        res = 1

        # Explore all four possible directions
        res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
        res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

        # Store the result in the cache
        dp[(r, c)] = res

        return res

    # Iterate through all positions in the matrix and run DFS
    for r in range(ROWS):
        for c in range(COLS):
            dfs(r, c, -1)

    # Find the maximum LIP from all positions and return it
    return max(dp.values())
