class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # tree -> add edge -> remove that edge -> tree

        # Valid Tree conditions...
        # 1. Connected
        # 2. No 

        # Cycle Detection, remove last edge in cycle


        # Union Find Solution
        # If we have 1 ... N nodes and we initially have a tree (no cycles), we have n - 1 edges at first
        # Union Find reveals the edge that causes the cycle (last edge added), so we just return this
        # TC: O(V + E)
        N = len(edges)
        par = [i for i in range(N + 1)] # ith node -> parent (1 - n)
        rank = [1] * (N + 1)

        def find(n):
            # find n's root parent
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

            

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            

            if rank[p1] > rank[p2]:
                # parent of p2 becomes p1
                par[p2] = p1
                rank[p1] += rank[p2]
                 
            else:
                # parent of p1 becomes p2
                par[p1] = p2
                rank[p2] += rank[p1]
            return True # if not already connected
        
        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1, n2]




        
        