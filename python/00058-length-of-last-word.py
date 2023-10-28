def lengthOfLastWord(self, s: str) -> int:
    # Initialize pointers
    i = len(s) - 1
    length = 0

    # Eliminate leading white spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count the characters of the last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length
