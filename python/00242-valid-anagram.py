def isAnagram(self, s: str, t: str) -> bool:
    # Check if the lengths of the strings are equal
    if len(s) != len(t):
        return False

    # Create a hash map to count character occurrences in string s
    count_s = {}

    # Count occurrences in string s
    for char in s:
        count_s[char] = 1 + count_s.get(char, 0)

    # Decrement counts based on characters in string t
    for char in t:
        if char not in count_s:
            return False
        count_s[char] -= 1
        if count_s[char] == 0:
            del count_s[char]

    # If the hash map is empty, the strings are anagrams
    return not count_s
