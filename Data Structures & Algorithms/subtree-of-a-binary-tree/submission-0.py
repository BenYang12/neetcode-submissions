# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base case
        #null is always subtree
        if not subRoot:
            return True
        if not root:
            return False
        
        #both trees not empty...

        if self.sameTree(root,subRoot):
            return True
      
        #not same subtree, recursively search left and right
        return (self.isSubtree(root.left,subRoot) or 
        self.isSubtree(root.right,subRoot))


    #helper function
    def sameTree(self, s, t):
        #base case 1 -> given empty trees
        if not s and not t:
            return True

        #base case 2 -> one empty one not empty
        if not s or not t:
            return False

        if s and t and s.val == t.val:
            return (self.sameTree(s.left,t.left) and 
            self.sameTree(s.right,t.right))




        