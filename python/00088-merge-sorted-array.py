def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Initialize pointers for the last positions in nums1, nums2, and the merged array.
    last = m + n - 1
    m -= 1
    n -= 1

    # Merge elements from the end to the beginning.
    while m >= 0 and n >= 0:
        if nums1[m] >= nums2[n]:
            nums1[last] = nums1[m]
            m -= 1
        else:
            nums1[last] = nums2[n]
            n -= 1
        last -= 1

    # Fill nums1 with any remaining elements from nums2 (if any).
    while n >= 0:
        nums1[last] = nums2[n]
        n -= 1
        last -= 1
