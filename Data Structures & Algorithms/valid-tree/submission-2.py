class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #no graph to traverse
        if n == 0:
            return False

        
        #create adjacency list
        adj = {i:[] for i in range(n)}


        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        
        #Now...we run DFS from each node
        #DFS function first
        #Prev param is needed during DFS 
        visit = set()
        def dfs(i, prev):
            #contract, return True or False if Cycle is detected using a set

            #base cases
            if i in visit:
                return False

            #recursive case 
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                
                if not dfs(j, i):
                    return False

            return True
        
        return dfs(0, -1) and len(visit) == n
        

                

                
            
                

                

            

            
           
        