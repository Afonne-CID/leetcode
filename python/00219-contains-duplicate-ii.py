def containsNearbyDuplicate(self, nums, k):
    # Initialize a set to keep track of values within the window
    window = set()
    # Initialize the left pointer of the window
    L = 0

    for R in range(len(nums)):
        # If the window size exceeds k, remove the leftmost value
        if R - L > k:
            window.remove(nums[L])
            L += 1
        # If the current value is already in the window, we found a duplicate
        if nums[R] in window:
            return True
        # Add the current value to the window
        window.add(nums[R])

    # If no duplicates were found, return False
    return False
