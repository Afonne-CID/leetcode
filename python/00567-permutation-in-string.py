def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1Count, s2Count = [0] * 26, [0] * 26

    # Initialize the count arrays for s1 and the initial window in s2
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s2[i]) - ord("a")] += 1

    matches = 0  # Number of character matches

    # Check if the initial window is a permutation of s1
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0

    l = 0  # Left pointer for the sliding window

    # Move the window to the right and update counts
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True  # We found a permutation

        # Update the counts for the new character on the right
        index = ord(s2[r]) - ord("a")
        s2Count[index] += 1

        # Update matches based on the changes
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        # Remove the character on the left and update counts
        index = ord(s2[l]) - ord("a")
        s2Count[index] -= 1

        # Update matches based on the changes
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1

        l += 1  # Move the left pointer

    return matches == 26  # Check matches for the last window
