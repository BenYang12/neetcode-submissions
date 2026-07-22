class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #create adj list {course: [prerequisites]}
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre) 

        # a course has three possible states
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle
        output = []
        cycle = set() #tracks current dfs path
        visit = set() #tracks fully processed courses
       
        def dfs(crs):
            #detect cycle
            if crs in cycle:
                return False
            if crs in visit:
                return True

            #recursively run dfs
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False: #DFS all prereqs first
                    return False
            cycle.remove(crs)

            visit.add(crs) #After processing prereqs, add the course to the result
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output