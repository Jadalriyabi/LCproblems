class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        # Map each course to its prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                #detected cycle
                return False
            
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            preMap[crs] = []
            
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
            
