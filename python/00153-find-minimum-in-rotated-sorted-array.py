def findMin(self, nums: List[int]) -> int:
    left, right = 0, len(nums) – 1
    result = nums[0]

    while left <= right:
        # If the subarray is already sorted, update the result and exit.
        if nums[left] <= nums[right]:
            result = min(result, nums[left])
            break

        mid = (left + right) // 2
        result = min(result, nums[mid])

        # Check if mid is in the left or right sorted portion.
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid – 1

    return result
