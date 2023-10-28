def countBits(n: int):
    # Initialize an array to store the results
    dp = [0] * (n + 1)

    # Offset is used to track the most significant bit
    offset = 1

    for i in range(1, n + 1):
        # If offset * 2 == i, update the offset
        if offset * 2 == i:
            offset = i
        # Calculate the number of ones based on the offset
        dp[i] = 1 + dp[i - offset]

    return dp
