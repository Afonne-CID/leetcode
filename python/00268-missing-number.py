def missingNumber(nums):
    result = len(nums)

    for i in range(len(nums)):
        result ^= i ^ nums[i]

    return result
