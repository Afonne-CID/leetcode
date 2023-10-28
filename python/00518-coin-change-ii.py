def change(amount, coins):
    # Create a 2D array to store results
    dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

    # Initialize base case: There's one way to make amount 0 with no coins.
    for i in range(len(coins) + 1):
        dp[i][0] = 1

    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if j >= coins[i - 1]:
                # Two choices: use the current coin or skip it
                use_coin = dp[i][j - coins[i - 1]]
                skip_coin = dp[i - 1][j]
                dp[i][j] = use_coin + skip_coin
            else:
                # If the current coin is too large to be used, skip it
                dp[i][j] = dp[i - 1][j]

    return dp[len(coins)][amount]
