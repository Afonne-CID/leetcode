def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)

    # Initialize a 2-D array to store the minimum operations.
    dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]

    # Base cases: If one string is empty, insert or delete all characters.
    for i in range(m + 1):
        dp[i][n] = m - i
    for j in range(n + 1):
        dp[m][j] = n - j

    # Fill the dp array using bottom-up dynamic programming.
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

    return dp[0][0]
