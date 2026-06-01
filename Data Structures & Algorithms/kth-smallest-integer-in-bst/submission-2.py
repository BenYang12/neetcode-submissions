# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.dfs(root, res)
        return res[k-1]

    
    def dfs(self, root, arr):

        if not root:
            return None
        
        self.dfs(root.left,arr)
        arr.append(root.val)
        self.dfs(root.right,arr)

        