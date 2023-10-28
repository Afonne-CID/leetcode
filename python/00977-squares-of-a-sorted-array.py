def sortedSquares(nums):
    # Initialize an array to store the result
    n = len(nums)
    result = [0] * n

    # Initialize pointers for the left and right ends of the input array
    left, right = 0, n - 1

    # Iterate from right to left, filling the result array with squared values
    while left <= right:
        # Get the absolute values of the elements at the left and right pointers
        left_value = abs(nums[left])
        right_value = abs(nums[right])

        # Compare the squared values and fill the result array accordingly
        if left_value > right_value:
            result[right - left] = left_value * left_value
            left += 1
        else:
            result[right - left] = right_value * right_value
            right -= 1

    return result
