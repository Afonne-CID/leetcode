def canFinish(numCourses, prerequisites):
    # Create a prerequisite map to store prerequisites for each course
    preMap = {i: [] for i in range(numCourses)}

    # Map each course to its prerequisites
    for course, prereq in prerequisites:
        preMap[course].append(prereq)

    # Set to keep track of currently visiting nodes during DFS
    visiting = set()

    # Depth-First Search function to check if courses can be completed
    def dfs(course):
        if course in visiting:
            return False  # Detected a cycle, return false
        if not preMap[course]:
            return True  # No prerequisites, course can be completed

        visiting.add(course)
        for prereq in preMap[course]:
            if not dfs(prereq):
                return False  # A prerequisite cannot be completed

        visiting.remove(course)
        preMap[course] = []  # Mark the course as completed
        return True

    # Iterate through each course and check if it can be completed
    for course in range(numCourses):
        if not dfs(course):
            return False  # If any course cannot be completed, return false

    return True  # All courses can be completed

# Example usage:
numCourses = 2
prerequisites = [[1, 0]]
result = canFinish(numCourses, prerequisites)
print(result)  # Output: True
