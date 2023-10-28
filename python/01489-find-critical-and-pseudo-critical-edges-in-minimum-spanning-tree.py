def findCriticalAndPseudoCriticalEdges(n, edges):
    def kruskal(edges, excluded_edge=None):
        # Sort the edges in ascending order of their weights
        edges.sort(key=lambda x: x[2])

        # Initialize UnionFind for tracking connected components
        uf = UnionFind(n)

        min_cost = 0
        mst_edges = []

        # First, add the excluded edge to MST if provided
        if excluded_edge:
            u, v, w = excluded_edge
            if uf.union(u, v):
                min_cost += w
                mst_edges.append([u, v])

        # Add edges to MST
        for edge in edges:
            u, v, w = edge
            if edge == excluded_edge:
                continue
            if uf.union(u, v):
                min_cost += w
                mst_edges.append([u, v])

        return min_cost, mst_edges

    # Step 1: Find the minimum cost of MST without excluding any edge
    min_cost, _ = kruskal(edges)

    critical = []  # List to store critical edges
    pseudo_critical = []  # List to store pseudo-critical edges

    for i in range(len(edges)):
        # Step 2: Attempt to construct MST with the current edge as the only excluded edge
        min_cost_exclude, _ = kruskal(edges, excluded_edge=edges[i])

        # Step 3: Check if the excluded edge is critical or pseudo-critical
        if min_cost_exclude > min_cost:
            critical.append(i)
        elif min_cost_exclude == min_cost:
            pseudo_critical.append(i)

    return [critical, pseudo_critical]
