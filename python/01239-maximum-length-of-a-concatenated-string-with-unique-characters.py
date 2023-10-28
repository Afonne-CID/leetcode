from collections import Counter

class Solution:
    def maxLength(self, arr):
        # Initialize a character set to track unique characters
        charSet = set()

        def overlap(charSet, s):
            # Check if there are overlapping characters
            c = Counter(charSet) + Counter(s)
            return max(c.values()) > 1

        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            res = 0
            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtrack(i + 1))  # Don't concatenate arr[i]

        return backtrack(0)
