class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map each course to prereq List
        prevMap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            prevMap[crs].append(pre)

        #visit set = all courses along current DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            
            if prevMap[crs] == []:
                return True

            
            #take course
            visitSet.add(crs)
            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False
            
            visitSet.remove(crs)
            prevMap[crs] = []


            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

            


        