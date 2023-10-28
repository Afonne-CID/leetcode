def maxCoins(nums):
    # Add implicit 1s at the beginning and end of the input array
    nums = [1] + nums + [1]
    n = len(nums)

    # Initialize a cache to store computed results
    cache = {}

    # Helper function to calculate the maximum coins in a subarray
    def burst(left, right):
        # Check if the result is already cached
        if (left, right) in cache:
            return cache[(left, right)]

        # Base case: If the subarray contains only one balloon, return its value
        if left + 1 == right:
            return 0

        max_coins = 0

        # Try bursting each balloon in the subarray
        for pivot in range(left + 1, right):
            coins = nums[left] * nums[pivot] * nums[right]
            coins += burst(left, pivot) + burst(pivot, right)
            max_coins = max(max_coins, coins)

        # Cache the result for this subarray
        cache[(left, right)] = max_coins
        return max_coins

    # Start the dynamic programming process
    return burst(0, n - 1)
