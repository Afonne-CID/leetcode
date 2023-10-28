def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    # Check if the lengths of s1 and s2 add up to the length of s3.
    if len(s1) + len(s2) != len(s3):
        return False

    # Initialize a 2D DP array to store intermediate results.
    dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]

    # Base case: If both strings are empty, we've successfully formed s3.
    dp[len(s1)][len(s2)] = True

    # Fill in the DP array from bottom to top and right to left.
    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                dp[i][j] = True
            if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                dp[i][j] = True

    return dp[0][0]
