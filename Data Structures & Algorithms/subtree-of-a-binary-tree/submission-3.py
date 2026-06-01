# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #to check whether one tree is a subtree of another, we do two things
        # 1. walk through every node of the main tree (root) using DFS
        # 2. At each node, check if the subtree starting here is exactly the same as subRoot

        #base case
        if not subRoot:
            return True 
        
        #base case 
        if not root:
            return False

        #base case, #if the two subtrees are the same
        if self.isSame(root,subRoot):
            return True
        

        #if not, continue checkign down left subtree and right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, node1, node2):
        if not node1 and not node2:
            return True
            
        if not node1 or not node2:
            return False
            
        if node1 and node2 and node1.val != node2.val:
            return False
            
        return self.isSame(node1.left, node2.left) and self.isSame(node1.right, node2.right)
        
    


       

        