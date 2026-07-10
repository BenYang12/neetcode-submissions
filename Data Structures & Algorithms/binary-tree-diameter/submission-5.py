# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #given root -> return diameter of tree

        #use dfs
        #each dfs function will modify a global max diameter variable, while returning the max height up the call stack

        self.res = 0

        def dfs(root):
            #contract ->return max height

            #base case
            if not root:
                return 0
            

            #recursive case
            left = dfs(root.left)
            right = dfs(root.right)

            self.res = max(self.res, left + right)

            return 1 + max(left,right)

        dfs(root)
        return self.res

