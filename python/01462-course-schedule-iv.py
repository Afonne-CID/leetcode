from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]) -> List[bool]:
        # Create an adjacency list to represent the prerequisites graph.
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        # Define a depth-first search (DFS) function to find indirect prerequisites.
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in adj[crs]:
                    prereqMap[crs] |= dfs(pre)
            prereqMap[crs].add(crs)
            return prereqMap[crs]

        # Initialize a dictionary to store the indirect prerequisites.
        prereqMap = {}

        # Build the prerequisites for each course using DFS.
        for crs in range(numCourses):
            dfs(crs)

        # Answer the queries by checking if u is in the prereqMap of v.
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res
