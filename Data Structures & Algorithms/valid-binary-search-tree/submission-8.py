# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # root -> return true if valid binary search tree, else false
        # recursive in nature -> DFS 


        # every node in left subtree must be less than root
        # every node in right subtree must be greater
        def dfs(node, left, right):
            if not node:
                return True
        
            if not left < node.val:
                return False
            
            if not right > node.val:
                return False
            

            return dfs(node.left, left, node.val ) and dfs(node.right, node.val, right)
        

        return dfs(root, float("-inf"), float("inf"))



        