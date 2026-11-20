# TC: O(n)
# SC: O(n) for recursion stack


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        # inverting binary tree -> swappping every node's left and right subtree
        # DFS -> use recursion to invert tree in top-down manner

        # 1. swap left and right children
        # 2. recursively invert left subtree
        # 3. recursively invert right subtree


        # base case 
        if not root:
            return None

        
        # pre-order dfs: process -> left -> right

        # process
        root.left, root.right = root.right, root.left


        # recursively call
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    

    
        



        