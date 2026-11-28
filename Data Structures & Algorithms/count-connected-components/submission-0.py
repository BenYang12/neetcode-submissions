class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Input: n = 5, edges = [[0,1], [1,2], [3,4]]
        # Output: 2

        # DFS
        # If we start DFS from unvisited node, we visit all nodes in its connected component
        # Every time we start DFS from a new unvisited node, we've found one new component
        # TC: O(E + V)
        # SC: O(E + V)


        # Build adjacency list
        adj = {i:[] for i in range(n)}
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        
        # DFS
        visited = set()
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        res = 0
        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node)
        
        return res
    
                


        