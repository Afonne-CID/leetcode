def hasAllCodes(s: str, k: int) -> bool:
    # Create a set to store unique binary codes of size k.
    code_set = set()

    # Iterate through every possible starting position in the string.
    for i in range(len(s) - k + 1):
        # Check if we can create a substring of size k starting at position i.
        # This ensures there are at least k - 1 characters after position i.
        if s[i : i + k] not in code_set:
            # Add the unique code to the set.
            code_set.add(s[i : i + k])

    # If the number of unique binary codes is equal to 2^k, return True; otherwise, return False.
    return len(code_set) == 2**k
