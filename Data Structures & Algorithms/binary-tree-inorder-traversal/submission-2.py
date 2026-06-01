# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inOrder(root,res)
        return res

    def inOrder(self, root,res):
        #base case
        if not root:
            return

        self.inOrder(root.left,res)
        res.append(root.val)
        self.inOrder(root.right,res)
        

        
        
        
        