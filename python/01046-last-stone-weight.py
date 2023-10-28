import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Use _heapify_max to create a max heap.
        heapq._heapify_max(stones)
        while len(stones) > 1:
            max_stone = heapq._heappop_max(stones)
            diff = max_stone - stones[0]
            if diff:
                heapq._heapreplace_max(stones, diff)
            else:
                heapq._heappop_max(stones)

        # If there's one stone left, return its value; otherwise, return 0.
        stones.append(0)
        return stones[0]
