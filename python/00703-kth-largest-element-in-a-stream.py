import heapq  # Import the heapq module

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Create a min-heap with k largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)  # Add the value to the min-heap
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)  # Remove the smallest element if size exceeds k
        return self.minHeap[0]  # Return the minimum value from the min-heap
