def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)  # Ensure k is within bounds.

    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    reverse(nums, 0, len(nums) - 1)       # Reverse the entire array.
    reverse(nums, 0, k - 1)               # Reverse the first k elements.
    reverse(nums, k, len(nums) - 1)       # Reverse the remaining elements.
