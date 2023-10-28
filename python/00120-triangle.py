def minimumTotal(triangle):
    dp = triangle[-1]  # Initialize dp with the last row of the triangle

    for row in range(len(triangle) - 2, -1, -1):
        for col in range(0, row + 1):
            dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

    return dp[0]
