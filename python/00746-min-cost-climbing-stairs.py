def minCostClimbingStairs(cost):


 # Append a 0 to the end of the cost array for simplicity.
    cost.append(0)

    # Initialize the dp array to store minimum cost.
    dp = [0] * len(cost)

    # Start from the second-to-last step and work backwards.
    for i in range(len(cost) - 3, -1, -1):
        dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

    # Minimum cost is the minimum of starting at index 0 or 1.
    return min(dp[0], dp[1])

# Example usage:
cost1 = [10, 15, 20]
print(minCostClimbingStairs(cost1))  # Output: 15

cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost2))  # Output: 6
