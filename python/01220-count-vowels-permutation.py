def countVowelPermutation(self, n: int) -> int:
    MOD = 10**9 + 7

    # Initialize dp with values for strings of length 1
    dp = [[0] * 5 for _ in range(n)]
    for i in range(5):
        dp[0][i] = 1

    # Fill in the dp array for strings of length 2 to n
    for length in range(1, n):
        dp[length][0] = (dp[length - 1][1] + dp[length - 1][2] + dp[length - 1][4]) % MOD
        dp[length][1] = (dp[length - 1][0] + dp[length - 1][2]) % MOD
        dp[length][2] = (dp[length - 1][1] + dp[length - 1][3]) % MOD
        dp[length][3] = (dp[length - 1][2]) % MOD
        dp[length][4] = (dp[length - 1][

2] + dp[length - 1][3]) % MOD

    # Calculate the total count for strings of length n
    total_count = sum(dp[n - 1]) % MOD

    return total_count
