# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diamter = length (# edges) of longest path between any two nodes
        # root -> diameter


        # path must go through some node (doesn't need to be root)
        # at that node, length of path = left subtree height + right subtree height

        # DFS
        # contract returns height
        # while doing dfs, update global diameter variable
        self.diameter = 0

        def dfs(node):

            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            self.diameter = max(self.diameter, left_height + right_height)


            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.diameter

