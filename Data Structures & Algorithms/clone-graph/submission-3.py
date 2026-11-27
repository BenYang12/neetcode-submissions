"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # reference of node in connected undirected graph -> return deep copy of the graph
        # deep copy: brand-new, independent duplicate of every node, edge, and nested data attribute in the original graph

        # DFS, HashMap
        # {old: new clone}
        # TC: O(n) = E + V

        # Intuition:
        # Graph may contain cycles
        # cannot simply copy nodes recursively w/o remembering what we've already copied
        # to handle this.. use a map (old -> new)


        # 1. When we first see a node, create its copy
        # 2. If we see same node again, reuse already-created copy
        # 3. This avoids infinite loops and ensures each node is cloned exactly once

        oldToNew = {} # {original: cloned}
        def dfs(node):
            # if node already in map -> return its clone
            if node in oldToNew:
                return oldToNew[node]
            
            # create a new node w/ same value, store it in map
            copy = Node(node.val)
            oldToNew[node] = copy

            # recursively clone all neighbors and add them to clone's neighbor list
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        

        return dfs(node) if node else None

            




       
        

            






        