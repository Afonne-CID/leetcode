def subsetsWithDup(nums):
    res = []
    nums.sort()

    def backtrack(i, subset):
        if i == len(nums):
            res.append(subset[:])  # Make a copy of the subset
            return

        # Include the current element
        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()

        # Skip the duplicates
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        # Exclude the current element
        backtrack(i + 1, subset)

    backtrack(0, [])
    return res
