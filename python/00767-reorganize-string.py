from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count the occurrences of each character
        count = Counter(s)

        # Step 2: Create a max-heap (implemented as a min-heap with negative counts)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""

        # Step 4: Pop the most frequent character and append it to the result string
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""  # Step 6: Return an empty string if not possible

            # Pop the most frequent character from the max-heap
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            # Update prev if count is not zero
            if cnt != 0:
                prev = [cnt, char]

        return res  # Step 7: Return the valid rearrangement

# Create an instance of the Solution class
solution = Solution()

# Example usage:
input_str = "aab"
output_str = solution.reorganizeString(input_str)
print(output_str)  # Output: "aba"
