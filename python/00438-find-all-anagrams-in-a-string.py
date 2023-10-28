def findAnagrams(s: str, p: str):
    # Initialize the start index, pMap, sMap, and the result list.
    startIndex = 0
    pMap, sMap = {}, {}
    res = []

    # Count the occurrences of each character in string p.
    for char in p:
        pMap[char] = 1 + pMap.get(char, 0)

    # Iterate through string s.
    for i in range(len(s)):
        # Count the occurrences of each character in the current window of s.
        sMap[s[i]] = 1 + sMap.get(s[i], 0)

        # Check if the current window size is equal to the length of p.
        if i >= len(p) - 1:
            # If the current window is an anagram of p, add its start index to the result.
            if sMap == pMap:
                res.append(startIndex)

            # If the character at the start index is in sMap, remove it and update the map.
            if s[startIndex] in sMap:
                sMap[s[startIndex]] -= 1
                if sMap[s[startIndex]] == 0:
                    del sMap[s[startIndex]]

            # Increment the start index.
            startIndex += 1

    return res
