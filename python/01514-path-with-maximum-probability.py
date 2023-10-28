import collections
import heapq

def maxProbability(n, edges, succProb, start, end):
    # Create an adjacency list to represent the graph.
    adj = collections.defaultdict(list)
    for i in range(len(edges)):
        src, dst = edges[i]
        adj[src].append((dst, succProb[i]))
        adj[dst].append((src, succProb[i]))

    # Priority queue for Dijkstra's algorithm. We use a Max Heap.
    pq = [(-1, start)]  # We start with a probability of -1 (inverse of 1).
    visited = set()

    while pq:
        prob, cur = heapq.heappop(pq)
        visited.add(cur)

        if cur == end:
            return -prob  # Return the maximum probability (negative due to Max Heap).

        for nei, edgeProb in adj[cur]:
            if nei not in visited:
                heapq.heappush(pq, (prob * edgeProb, nei))

    return 0.0  # If no path is found, return 0.0.

# Example usage
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
result = maxProbability(n, edges, succProb, start, end)
print("Maximum Probability (Dijkstra's Algorithm):", result)
