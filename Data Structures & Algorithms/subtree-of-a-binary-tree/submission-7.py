# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # root, subRoot -> return True if there exists subtree of root w/ same structure and values of subRoot, false otherwise

        # dfs 
        # base cases
        # 1. subRoot is null
        if not subRoot:
            return True
        
        # 2. root is null
        if not root:
            return False
        
        # 3. same tree
        if self.sameTree(root, subRoot):
            return True
        

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        

    def sameTree(self, p, q):
        # DFS
        # Base case 1: both null
        if not p and not q:
            return True
            
        # Base case 2: one null
        if not p or not q:
            return False

        # Base case 3: both non-null different val
        if p.val != q.val:
            return False
            

        return self.sameTree(p.left,q.left) and self.sameTree(p.right, q.right)

        