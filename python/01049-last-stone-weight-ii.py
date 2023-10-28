def lastStoneWeightII(stones):
    # Calculate the sum of all stone weights
    stoneSum = sum(stones)
    # Calculate the target weight for each pile
    target = (stoneSum + 1) // 2

    # Helper function for dynamic programming
    def dfs(i, total):
        # Base cases
        if total >= target or i == len(stones):
            return abs(total - (stoneSum - total))
        if (i, total) in dp:
            return dp[(i, total)]

        # Choose not to include the current stone
        not_included = dfs(i + 1, total)
        # Choose to include the current stone
        included = dfs(i + 1, total + stones[i])

        # Update the cache with the minimum of the two choices
        dp[(i, total)] = min(not_included, included)
        return dp[(i, total)]

    # Initialize the cache
    dp = {}
    # Start the dynamic programming process
    return dfs(0, 0)
