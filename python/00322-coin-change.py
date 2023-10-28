def coinChange(coins, amount):
    # Initialize a DP array to store the minimum number of coins for each amount.
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    # Iterate through all possible amounts from 1 to the target amount.
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != amount + 1 else -1
