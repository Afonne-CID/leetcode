def largestNumber(self, nums: List[int]) -> str:
    # Convert integers to strings
    for i, n in enumerate(nums):
        nums[i] = str(n)

    # Custom comparison function
    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1

    # Sort the numbers based on the custom comparison
    nums = sorted(nums, key=cmp_to_key(compare))

    # Concatenate and return the result as a string
    return str(int("".join(nums)))
