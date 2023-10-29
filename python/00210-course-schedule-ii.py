def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    def build_adjacency_list(numCourses, prerequisites):
        # Initialize the adjacency list with empty lists for each course
        prereq = {c: [] for c in range(numCourses)}

        # Populate the adjacency list based on prerequisites
        for course, prereq_course in prerequisites:
            prereq[course].append(prereq_course)

        return prereq

    def dfs(course):
        if course in cycle:
            return False
        if course in visit:
            return True

        cycle.add(course)
        for prereq in prereq_map[course]:
            if not dfs(prereq):
                return False
        cycle.remove(course)
        visit.add(course)
        order.append(course)
        return True

    prereq_map = build_adjacency_list(numCourses, prerequisites)
    order = []
    visit, cycle = set(), set()

    for course in range(numCourses):
        if not dfs(course):
            return []

    return order  # Do not reverse the order