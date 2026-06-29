# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #given root -> return diameter (longest path between any two nodes in a tree)
        #longest path might not necessarily run through the root
        #naive -> try to calculate diamter through every single node in tree (height on left + height on r) through recursive alg with DFS
        #however, DFS returns height up, not the diameter

        self.res = 0


        #does not return diameter, returns the height
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left,right)

        dfs(root)

        return self.res

            
        
        
        