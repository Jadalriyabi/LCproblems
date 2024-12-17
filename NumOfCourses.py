class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize a map to store each course and its prerequisites
        preMap = {i: [] for i in range(numCourses)}

        # Populate the map with prerequisites for each course
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # A set to keep track of courses being visited in the current DFS path
        visiting = set()

        # Depth-first search (DFS) function to detect cycles
        def dfs(crs):
            # If the course is already in the visiting set, a cycle is detected
            if crs in visiting:
                return False  # Cycle found, so we cannot complete the courses
            
            # If the course has no prerequisites, it can be completed
            if preMap[crs] == []:
                return True
            
            # Mark the course as being visited
            visiting.add(crs)

            # Recursively check all prerequisites for the current course
            for pre in preMap[crs]:
                if not dfs(pre):  # If a cycle is found, return False
                    return False

            # Remove the course from the visiting set as the DFS is complete
            visiting.remove(crs)

            # Mark the course as having no prerequisites (optimization step)
            preMap[crs] = []

            return True  # Course can be completed
        
        # Check all courses to ensure they can be completed
        for c in range(numCourses):
            if not dfs(c):  # If a cycle is detected, return False
                return False

        # If no cycles are detected, all courses can be completed
        return True
