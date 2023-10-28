def longestConsecutive(self, nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if (num – 1) not in num_set:  # Check if it’s the start of a sequence
            length = 1
            while (num + length) in num_set:  # Continue to extend the sequence
                length += 1
            longest = max(length, longest)

    return longest
