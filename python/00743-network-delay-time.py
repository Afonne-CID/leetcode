def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # Initialize a dictionary to store the graph's edges (adjacency list).
    edges = collections.defaultdict(list)

    # Populate the adjacency list with the edges.
    for u, v, w in times:
        edges[u].append((v, w))

    # Initialize a min-heap to track nodes to visit, starting with (0, k).
    minHeap = [(0, k)]

    # Initialize a set to keep track of visited nodes.
    visit = set()

    # Initialize a variable to track the time taken.
    t = 0

    # Perform the Dijkstra's algorithm using a min-heap.
    while minHeap:
        # Pop the node with the minimum weight.
        w1, n1 = heapq.heappop(minHeap)

        # If the node has already been visited, continue.
        if n1 in visit:
            continue

        # Mark the node as visited and update the time.
        visit.add(n1)
        t = w1

        # Explore the neighbors of the current node.
        for n2, w2 in edges[n1]:
            if n2 not in visit:
                # Add the neighbor to the min-heap with updated weight.
                heapq.heappush(minHeap, (w1 + w2, n2))

    # If we visited all nodes, return the time; otherwise, return -1.
    return t if len(visit) == n else -1
