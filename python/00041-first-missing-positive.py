def firstMissingPositive(self, nums: List[int]) -> int:
    # Step 1: Eliminate negative values and values greater than the array length
    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] > len(nums):
            nums[i] = len(nums) + 1

    # Step 2: Mark positive integers by changing the sign
    for num in nums:
        index = abs(num)
        if 1 <= index <= len(nums):
            if nums[index - 1] > 0:
                nums[index - 1] *= -1

    # Step 3: Find the smallest missing positive integer
    for i in range(len(nums)):
        if nums[i] > 0:
            return i + 1

    # If all positive integers are present, return the next positive integer
    return len(nums) + 1
