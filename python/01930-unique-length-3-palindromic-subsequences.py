def countPalindromicSubsequence(s: str) -> int:
    result = set()  # To store unique palindromes
    left = set()    # Characters to the left of the middle character
    right = {}      # Characters to the right of the middle character and their counts

    for i in range(1, len(s)):  # Starting from the second character
        middle = s[i]

        # Update the right hash map
        if middle in right:
            right[middle] += 1
        else:
            right[middle] = 1

        # Check for valid three-length palindromes
        for j in range(26):
            c = chr(ord('a') + j)  # Generate characters from 'a' to 'z'
            if c in left and c in right:
                result.add((middle, c))  # Add the palindrome to the result set

        # Update the left hash set
        left.add(middle)

        # Update the right hash map by decrementing the count
        if s[i - 1] in right:
            right[s[i - 1]] -= 1
            if right[s[i - 1]] == 0:
                right.pop(s[i - 1])

    return len(result)
