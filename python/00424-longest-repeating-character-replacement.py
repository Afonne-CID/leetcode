def characterReplacement(self, s: str, k: int) -> int:
    # Initialize variables
    counts = {}  # Dictionary to store character counts in the current window
    max_length = 0  # Maximum valid substring length
    left = 0  # Left pointer

    # Iterate through the string using the right pointer
    for right in range(len(s)):
        # Update the character count in the window
        counts[s[right]] = 1 + counts.get(s[right], 0)

        # Find the maximum character count in the current window
        max_count = max(counts.values())

        # Check if the window is valid (replacements needed <= k)
        if (right - left + 1) - max_count > k:
            # The window is not valid, so increment the left pointer
            counts[s[left]] -= 1
            left += 1

        # Update the maximum valid substring length
        max_length = max(max_length, right - left + 1)

    return max_length
