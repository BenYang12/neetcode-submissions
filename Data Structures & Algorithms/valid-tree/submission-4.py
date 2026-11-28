class Solution:
    # TC: O(V + E)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
        # Output: true 

        # Graph is valid tree if:
        # 1. No Cycles
        # 2. Fully connected

        # Convert to adjacency list, use DFS to detect cycles
        # Check if number of nodes visited aka len(set) == n to check connection

        # Edge case: no graph to traverse
        if n == 0:
            return False

        # adjacency list
        adj = {i:[] for i in range(n)}
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        
        # DFS
        # pass in prev to prevent going backwards and loop false positive
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False

            
            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
        

    



        
        