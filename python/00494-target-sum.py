def findTargetSumWays(nums, target):
    # Create a cache to store computed results
    dp = {}

    def backtrack(index, total):
        # Base case
        if index == len(nums):
            return 1 if total == target else 0

        # Check if this state is already computed
        if (index, total) in dp:
            return dp[(index, total)]

        # Calculate the number of ways by adding and subtracting
        ways_add = backtrack(index + 1, total + nums[index])
        ways_subtract = backtrack(index + 1, total - nums[index])

        # Store the result in the cache
        dp[(index, total)] = ways_add + ways_subtract

        return dp[(index, total)]

    # Start the recursion with initial values
    return backtrack(0, 0)
