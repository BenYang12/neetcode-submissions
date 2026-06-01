# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False
            
            if node1 and node2 and node1.val != node2.val:
                return False
            
            return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)


        #base case 1
        if not subRoot:
            return True
        
        #base case 2
        if not root:
            return False
        
        #if they have same structure and value
        if isSame(root, subRoot):
            return True
        
        #if they are not equal nodes
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        


        