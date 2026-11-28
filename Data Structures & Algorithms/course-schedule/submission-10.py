class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Input: numCourses = 2,  prerequisites = [[1, 0]]
        # Output: Is it possible to finish all courses? -> True

        # If cycle -> return False!
        # solve using DFS, adjacency list! 
        # Goal: for each node, can we complete it?
        # Base case: course has no prerequisite, return []
        # detect loop with a set
        

        # TC: O(n + p)


        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        visit = set() # all courses along cur DFS path
        def dfs(crs):
            # contract: return boolean 
            # base case
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            preMap[crs] = []
            
            
            
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
                    









        