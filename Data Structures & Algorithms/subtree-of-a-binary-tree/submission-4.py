# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #To check whether one tree is a subtree of another...
        #1. Walk through every node of the main tree (root) using DFS
        #2. At each node, check if the subtree starting here is exactly the same as subRoot

        #base case
        if not subRoot:
            return True

        #base case
        if not root:
            return False

        #in this case, both subRoot and root are not null
        #base case
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)



    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if root.val != subRoot.val:
            return False

        
        return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))

        