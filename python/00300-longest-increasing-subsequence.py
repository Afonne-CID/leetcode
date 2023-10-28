def lengthOfLIS(nums):
    # Initialize a list to store the length of LIS for each element in nums
    lis = [1] * len(nums)

    # Iterate through the elements in reverse order
    for i in range(len(nums) - 1, -1, -1):
        # Iterate through elements that come after the current element
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                # Update the lis for the current element
                lis[i] = max(lis[i], 1 + lis[j])

    # Return the maximum value in lis, which represents the length of the longest increasing subsequence
    return max(lis)
