def uniquePathsWithObstacles(self, grid: List[List[int]) -> int:
    M, N = len(grid), len(grid[0])
    dp = [[0] * N for _ in range(M)]

    # Initialize the bottom-right cell
    dp[M-1][N-1] = 1

    # Iterate through the grid in reverse order
    for r in reversed(range(M)):
        for c in reversed(range(N)):
            if grid[r][c]:
                dp[r][c] = 0
            else:
                if r + 1 < M:
                    dp[r][c] += dp[r + 1][c]
                if c + 1 < N:
                    dp[r][c] += dp[r][c + 1]

    return dp[0][0]
