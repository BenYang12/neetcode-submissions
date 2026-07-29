class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # return valid ordering (topological sort) of courses I take to finish all courses
        # not possible -> return empty array

        #first, create adj list
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        # then, from every crs...
        # run dfs from every course
        # check for cycles -> set
        # skip over courses that are already processed
        # base case -> append to output
        res = []
        visiting = set()
        visited = set()
        def dfs(crs):
            if crs in visiting:
                return False #cycle -> return False
            
            if crs in visited:
                return True #we've already put this into the output, no need, just return up
   
            
            #recursively run dfs
            visiting.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False #DFS all pre-reqs first
            visiting.remove(crs)
        
            #this specific crs is provabley reachable, so now lets process it
            visited.add(crs)
            res.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
        

        

            


    
        





        



        