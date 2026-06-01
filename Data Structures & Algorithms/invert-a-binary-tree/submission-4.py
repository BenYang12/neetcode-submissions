# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #DFS inorder traversal

        #base case
        if not root:
            return None

        #process node
        tmp = root.right
        root.right = root.left
        root.left = tmp

        #recursive case
        self.invertTree(root.left)
        self.invertTree(root.right)

        #confused here
        return root



        