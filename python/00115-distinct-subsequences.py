def numDistinct(s: str, t: str) -> int:
    # Initialize a cache to store computed results
    cache = {}

    # Helper function for depth-first search
    def dfs(i, j):
        # Base case 1: If t is empty, there is one way to match it (skip all characters in s).
        if j == len(t):
            return 1

        # Base case 2: If s is empty and t is not, there's no way to match t.
        if i == len(s):
            return 0

        # If the result for these indices is already cached, return it.
        if (i, j) in cache:
            return cache[(i, j)]

        # If the characters at s[i] and t[j] match, we have two options:
        # 1. Include the character in the subsequence (move both i and j).
        # 2. Skip the character in s (move only i).
        if s[i] == t[j]:
            result = dfs(i + 1, j + 1) + dfs(i + 1, j)
        else:
            # If characters don't match, we can only skip in s (move only i).
            result = dfs(i + 1, j)

        # Cache the result for these indices and return it.
        cache[(i, j)] = result
        return result

    # Start the depth-first search from the beginning of both strings.
    return dfs(0, 0)
