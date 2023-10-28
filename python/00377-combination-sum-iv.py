def combinationSum4(nums, target):
    # Initialize a dictionary to store intermediate results
    dp = {0: 1}

    # Iterate through the range of 1 to target
    for total in range(1, target + 1):
        dp[total] = 0
        for n in nums:
            dp[total] += dp.get(total - n, 0)
    return dp[target]
