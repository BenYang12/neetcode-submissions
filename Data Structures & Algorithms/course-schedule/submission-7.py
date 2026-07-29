class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # return true if I can finish all courses -> no cycles 
        # create adj list, run DFS from every single course. If nothing returns false, then I can return True overall
        adj = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            
            if adj[crs] == []:
                return True

            visiting.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False

            #backtracking pattern is needed here
            visiting.remove(crs)
            adj[crs] = []

            return True #return True at very end

            
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


    
        