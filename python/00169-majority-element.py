def majorityElement(nums):
    count = 0  # Initialize count
    result = None  # Initialize result

    for num in nums:
        if count == 0:
            result = num
        count += 1 if num == result else -1

    return result
