# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #BST where all values are unique, p and q
        #can do this iteratively
        #find the place where p and q split
        curr = root


        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

        



        