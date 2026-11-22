# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # TC: O(n)
        # SC: O(n)

        # node is "good" if on path from root to that node,
        # no earlier node has val greater than it


        # while traversing, carry maximum value seen so far 
        # if current node's value >= max -> it's a good node

        # start DFS from root and store root's value as current maxSoFar

        def dfs(node, maxVal):
            # contract = return # of "good nodes"
            # base case
            if not node:
                return 0


            # process -> then left -> then right
            if node.val >= maxVal:
                res = 1
                maxVal = max(maxVal, node.val)
            else:
                res = 0
           
            # leap of faith
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)
        


            
            
            






        
       