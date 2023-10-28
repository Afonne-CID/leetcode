def subsets(nums):
    res = []  # The list to store subsets

    def backtrack(start=0, subset=[]):
        res.append(subset[:])  # Add a copy of the current subset to the result
        for i in range(start, len(nums)):
            subset.append(nums[i])  # Include the current element
            backtrack(i + 1, subset)  # Recursively generate subsets
            subset.pop()  # Backtrack by removing the current element

    backtrack()  # Start the backtracking process
    return res
