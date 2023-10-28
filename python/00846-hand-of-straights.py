def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize:
        return False

    count = collections.Counter(hand)  # Count occurrences of each card value
    minHeap = list(count.keys())  # Unique card values

    heapq.heapify(minHeap)  # Convert to a min-heap

    while minHeap:
        first = minHeap[0]  # Get the minimum value from the min-heap
        for i in range(first, first + groupSize):
            if i not in count:
                return False
            count[i] -= 1
            if count[i] == 0:
                heapq.heappop(minHeap)

    return True
