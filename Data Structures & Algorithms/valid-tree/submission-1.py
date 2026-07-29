class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #no graph to traverse
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            #undirected edges
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        #prev is needed so we don't get false positives for loop detection
        def dfs(i, prev):
            #contract -> return True or False if cycle is detected using a sert

            #base case
            if i in visit:
                return False
            
            visit.add(i)

            #go through every neighbor in i
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False #detected loop -> immediately return false
            
            return True
        
        return dfs(0, -1) and len(visit) == n
            



        
    