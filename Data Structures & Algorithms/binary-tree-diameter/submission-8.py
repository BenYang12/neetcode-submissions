# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter =  longest path between any two nodes
        # this path must go through some node, and at that node the path length:
        # (left subtree height + right subtree height)


        # while doing a DFS to compute heights, simultaneously track...
        # max left + right seen so far
        # this gives diameter in one pass without recomputing heights


        self.res = float("-inf")
        def dfs(node):
            # CONTRACT: returns HEIGHT of subtree

            # base case
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            diameter = left_height + right_height
            self.res = max(self.res, diameter)

            # return height of current subtree
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.res

          



     
        



        