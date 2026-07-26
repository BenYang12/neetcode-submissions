class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #return valid ordering of courses I can take to finish all courses. 
        #if there are many valid answers, return any of them
        # if not possible, return empty array


        #step 1: create adj list
        prereq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        
        #A course has three possible states
        # visited -> crs has been appended to output
        # visiting -> crs not added to output, but added to cycle set
        # unvisited -> not added to output or cycle
        output = []
        cycle = set() #tracks current dfs path
        visit = set() #tracks fully processed courses

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            

            #recursively run DFS
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False #DFS all pre-reqs first
            cycle.remove(crs) #backtracking template

            #this course is reachable, so now lets process it!
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

        