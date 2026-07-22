class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create adjacency list
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        #visitSet = all courses along current DFS path
        visitSet = set()

        def dfs(crs):
            #base case
            if crs in visitSet:
                return False
            if adj[crs] == []:
                return True

            visitSet.add(crs) #currently visit 
            for pre in adj[crs]:
                if not dfs(pre): 
                    return False #recursively run DFS on each pre
            visitSet.remove(crs) # already finished visiting it, backtrack
            adj[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):return False
        return True

        #two separate graphs that are not connected -> calld dfs from every