# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #problem is recursive by nature -> Recursive DFS
        #at each node, swap left and right children
        #then recursively invert left subtree and then recursively invert right subtree

        #base case
        if not root:
            return 


        #process root
        tmp = root.right
        root.right = root.left
        root.left = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)


        return root
    


        