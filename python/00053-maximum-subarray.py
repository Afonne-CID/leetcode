def maxSubArray(nums):
    max_sum = nums[0]  # Initialize max_sum with the first element of the array.
    current_sum = 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        # If the current sum becomes negative, reset it to zero.
        if current_sum < 0:
            current_sum = 0

    return max_sum
