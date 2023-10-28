def maxSubarraySumCircular(self, nums: List[int]) -> int:
    # Initialize variables for global maximum and minimum
    globMax, globMin = nums[0], nums[0]
    # Initialize variables for current maximum and minimum
    curMax, curMin = 0, 0
    # Initialize a variable to calculate the total sum of the array
    total = 0

    # Iterate through the input array
    for i, n in enumerate(nums):
        # Update the current maximum
        curMax = max(curMax + n, n)
        # Update the current minimum
        curMin = min(curMin + n, n)
        # Calculate the total sum of the array
        total += n
        # Update the global maximum
        globMax = max(curMax, globMax)
        # Update the global minimum
        globMin = min(curMin, globMin)

    # Return the maximum of two possible results:
    # 1. The global maximum (non-circular subarray)
    # 2. The total sum minus the global minimum (circular subarray)
    return max(globMax, total - globMin) if globMax > 0 else globMax
