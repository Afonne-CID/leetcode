from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Convert input nums into a set for quick lookup
        strSet = set(nums)

        def backtrack(i, cur):
            # Base case: Check if we've generated a binary string of length n
            if i == len(nums):
                res = "".join(cur)
                return res if res not in strSet else None

            # Recursive call with '0' at the current position
            res = backtrack(i + 1, cur)
            if res:
                return res

            # Recursive call with '1' at the current position
            cur[i] = "1"
            res = backtrack(i + 1, cur)
            if res:
                return res

        # Start the backtracking with an initial string of all '0's
        return backtrack(0, ["0" for _ in range(len(nums))])
