# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p, q -> return True if trees are equivalent, else False
        # exact same structure, and nodes have the same values
        
        # DFS 
        # base cases

        # 1. both null
        if not p and not q:
            return True

        # 1. different structure
        if not p or not q:
            return False
         
        # 2. same structure, different values
        if p.val != q.val:
            return False

        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        