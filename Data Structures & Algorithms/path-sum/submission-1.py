# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curSum = 0
        
        def dfs(node, curSum):
            #base case, empty root
            if not node:
                return False 
            curSum += node.val

            if not node.left and not node.right:
                if curSum == targetSum:
                    return True
            
            return (dfs(node.left, curSum) or dfs(node.right, curSum))
        
        return dfs(root,0)

                



        