def removeDuplicates(nums):
    left = 0
    right = 0

    while right < len(nums):
        count = 1

        # Count duplicates
        while right + 1 < len(nums) and nums[right] == nums[right + 1]:
            right += 1
            count += 1

        # Keep at most two duplicates
        for i in range(min(2, count)):
            nums[left] = nums[right]
            left += 1

        right += 1

    return left
