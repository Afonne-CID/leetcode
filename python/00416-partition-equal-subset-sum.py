def canPartition(nums):
    # Check if the sum of the array is odd, if so, it's impossible to partition
    if sum(nums) % 2:
        return False

    # Initialize a set to store possible sums
    dp = set()
    dp.add(0)  # We can always achieve a sum of 0 with no elements
    target = sum(nums) // 2

    # Iterate through the array in reverse order
    for i in range(len(nums) - 1, -1, -1):
        nextDP = set()  # Create a new set for the next iteration
        for t in dp:
            if (t + nums[i]) == target:
                return True  # We found a subset that sums up to half the total
            nextDP.add(t + nums[i])
            nextDP.add(t)
        dp = nextDP

    return False  # If we can't find a valid partition, return False
