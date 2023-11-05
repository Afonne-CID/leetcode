def searchInsert(self, nums, target):
    # `O(log n)` time complexity and `O(1)` space complexity

    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid
    return left
  
