class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Input: numCourses = 3, prerequisites = [[1,0]]
        # Output: [0,1,2]

        # Intuition:
        # Each course is a node, each prereq is a directed edge
        # Want order s.t. all prereqs of course are taken before it

        # DFS, Adjacency List, Set: 
        # 1. Detect cycles (impossible to finish all courses)
        # 2. Add a course to the result after all its prereqs are processed

        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        

        # Then, run dfs from every course
        # Check for cycles -> set()
        # Skip over courses that are already processed 
        # base case -> append to output
        res = []
        visiting = set() # tracks current DFS path (for cycle detection)
        visit = set() # tracks fully processed courses

       
        def dfs(crs):
            # Contract: return boolean if reachable
            # base case(s)
            if crs in visiting:
                return False # cycle -> return False
            
            if crs in visit:
                return True # in visit -> already put in output
            

            # recursively run dfs
            visiting.add(crs)
            for pre in adj[crs]:
                if not dfs(pre): return False # DFS all pre-reqs first
            visiting.remove(crs)


            # this specific crs is provabley reachable, process it
            visit.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
            
        return res





        