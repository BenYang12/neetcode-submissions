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

        if not root:
            return None

        #"process root,swap children"
        tmp = root.left
        root.left = root.right
        root.right = tmp

        #left subtree
        self.invertTree(root.left)

       

        #right subtree
        self.invertTree(root.right)


        #return root at end of function so the caller receives the modified tree
        return root








      
    


        