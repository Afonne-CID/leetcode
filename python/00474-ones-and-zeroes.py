def findMaxForm(strs, m, n):
    # Create a 3D dynamic programming array
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]

    for i in range(1, len(strs) + 1):
        # Get the count of 0's and 1's in the current string
        mCnt, nCnt = strs[i - 1].count("0"), strs[i - 1].count("1")

        for mRemaining in range(m + 1):
            for nRemaining in range(n + 1):
                # Decision 1: Skip the current string
                dp[i][mRemaining][nRemaining] = dp[i - 1][mRemaining][nRemaining]

                # Decision 2: Include the current string if possible
                if mRemaining >= mCnt and nRemaining >= nCnt:
                    dp[i][mRemaining][nRemaining] = max(
                        dp[i][mRemaining][nRemaining],
                        1 + dp[i - 1][mRemaining - mCnt][nRemaining - nCnt]
                    )



 # Return the maximum size of the valid subset
    return dp[len(strs)][m][n]
