# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #recursive DFS
        #check structure and value

        #base case: both null
        if not p and not q:
            return True
        

        #base case: one null one not
        if not p or not q:
            return False
        
        #base case:
        if p.val != q.val:
            return False

        #otherwise, compare left subtree and right subtrees recursively

        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        