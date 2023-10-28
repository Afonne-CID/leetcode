import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        minHeap = []
        res = {}

        for query in queries:
            while intervals and intervals[0][0] <= query:
                left, right = intervals.pop(0)
                heapq.heappush(minHeap, (right - left + 1, right))

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            if minHeap:
                res[query] = minHeap[0][0]
            else:
                res[query] = -1

        result = [res[query] for query in queries]
        return result
