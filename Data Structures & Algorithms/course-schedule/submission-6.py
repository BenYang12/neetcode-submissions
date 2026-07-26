class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #return true if it is possible to finish all courses, otherwise return false
        #if I detect a cycle, I will return False
        #DFS or BFS can be used

        # DFS: how can I tell if a course can be completed?: no pre-reqs -> completable -> base case!
        # While DOING DFS, keep track of courses in current recursion path. If we visit a course already in the current path -> cycle found
        # If a course has no prerequisites left, it's safe
        # Use a set to detect cycles, adjacency list is perfect for this problem, as I can map node: [list of pre-reqs]


        #first step -> build a graph where each course points to its pre-reqs. create adjacency list
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        #visiting set to track curent DFS path
        #For each course, run DFS. if course is already in visiting -> return false (base case), "Course A needs B, which needs C, which NEEDS A." Then, recursively DFS its prerequisites
        #after succesfully processing a course, clear its prerequisite link (mark as done)
        #if all courses are processed without cycles, return true
        #if we can complete every single course, we can return true
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
    
            if adj[crs] == []:
                return True

            #recursive part
            visiting.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            #backtracking pattern is needed here!
            visiting.remove(crs)
            adj[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


        

       

    



        