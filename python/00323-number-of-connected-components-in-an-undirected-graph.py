from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]) -> int:
        # Initialize Union Find data structure.
        dsu = UnionFind()

        # Iterate through the edges and union the nodes.
        for a, b in edges:
            dsu.union(a, b)

        # Create a set of unique root parents and return its size as the number of components.
        return len(set(dsu.find(x) for x in range(n))
