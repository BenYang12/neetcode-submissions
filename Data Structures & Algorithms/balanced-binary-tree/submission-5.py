# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # root -> true if height-balanced, false otherwise
        # left and right subtrees of EVERY node

        # DFS 
        # return [balanced, height]
        # balanced is to ensure subtrees are balanced

        def dfs(node):
            # contract -> return [balanced, height]
            if not node:
                return [True, 0]

            
            leftSubtree = dfs(node.left)
            rightSubtree = dfs(node.right)
            balanced = leftSubtree[0] and rightSubtree[0] and abs(leftSubtree[1] - rightSubtree[1]) <= 1


            return [balanced, 1 + max(leftSubtree[1], rightSubtree[1])]
        

        return dfs(root)[0]



        