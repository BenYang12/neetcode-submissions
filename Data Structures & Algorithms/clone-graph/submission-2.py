"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #reference of a node in a connected undirected graph -> return deep copy
        oldToNew = {} #old node: new node

        def clone(node):
            #take original node, and creating a clone of that node, and cloning all of its nieghbors recursively.

            #check if node is in hashmap. yes -> we already made a clone -> return that clone
            if node in oldToNew:
                return oldToNew[node]
            
            #if above statement doesn't run, then clone doesn't already exist
            copy = Node(node.val)
            oldToNew[node] = copy #map old node to copy

            # make copies of every single neighbor
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy

        return clone(node) if node else None



        