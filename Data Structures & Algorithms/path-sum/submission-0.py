# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, curSum):
            #empty tree
            if not node:
                return False

            #if root is not null, add it to curSum
            curSum += node.val

            #reached a leaf node
            if not node.left and not node.right:
                if curSum == targetSum:
                    return True
            
            #if not a leaf node, run dfs on left and right sides
            #if either of these returns true, we can return true
            return dfs(node.left, curSum) or dfs(node.right, curSum)
        
        return dfs(root, 0)

                
            
          

            
            




      
        

        