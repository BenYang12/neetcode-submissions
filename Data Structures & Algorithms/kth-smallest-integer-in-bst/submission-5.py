# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # root of bst, k -> return kth smallest value (1-indexed) in the tree
        # bst: to go in ascending order -> inorder dfs aka left -> root -> right

        res = []


        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            # [1, 2, 3]

        dfs(root)
        return res[k -  1]
        




            
        