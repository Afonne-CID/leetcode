def minCostConnectPoints(points):
    # Get the number of points
    N = len(points)

    # Create an adjacency list to represent the graph
    adj = {i: [] for i in range(N)}  # i: list of [cost, node]

    # Calculate the distances and populate the adjacency list
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i + 1, N):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])

    # Prim's algorithm
    res = 0  # Total cost
    visit = set()  # Set to keep track of visited nodes
    minH = [[0, 0]]  # Min heap to keep track of edges [cost, point]

    while len(visit) < N:
        cost, i = heapq.heappop(minH)  # Pop the minimum cost edge
        if i in visit:
            continue
        res += cost  # Add the cost to the result
        visit.add(i)  # Mark the node as visited

        # Add neighbors to the min heap
        for neiCost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minH, [neiCost, nei])

    return res
