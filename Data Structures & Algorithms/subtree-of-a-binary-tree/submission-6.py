# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #base case -> null subRoot can be subroot of anything
        if not subRoot:
            return True
        
        #base case -> subRoot exists but root is null -> no subroot possible
        if not root:
            return False
        

        #base case -> same node value  -> check if same tree at that location
        if root.val == subRoot.val:
            if self.sameTree(root,subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)



    
    def sameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

    
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        