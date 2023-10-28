def maxProduct(nums):
    n = len(nums)
    result = nums[0]
    current_min = current_max = 1

    for num in nums:
        # Temporary variable to hold the current max
        temp = current_max

        # Calculate the new current max
        current_max = max(num, num * current_max, num * current_min)

        # Update the current min
        current_min = min(num, num * temp, num * current_min)

        # Update the overall result
        result = max(result, current_max)

    return result
