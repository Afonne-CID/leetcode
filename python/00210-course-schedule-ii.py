def findOrder(numCourses, prerequisites):
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

    return order[::-1]  # Reverse the order to get the correct course sequence
