# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        #use dfs to compute height of every subtree
        def dfs(root):
            #For each node during DFS, recursively get left height, recursively get right height, diameter through this node = left + right, update global answer with the diameter
            #Postorder DFS

            #base case
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            self.res = max(self.res, left + right)

            #return height
            return 1 + max(left,right)
        
        dfs(root)
        return self.res



        