# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #why do I need recursive dfs helper? -> I'm returning both a height and boolean!


        def dfs(root):

            #base case
            if not root:
                return [True,0]

            left,right = dfs(root.left), dfs(root.right)

            #from root node, is it balanced? How to determine?
            #if either of the left or right parameters return false -> we know for sure entire tree is not balanced. 
            #not only balanced at root, but also entire tree is balanced at all
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1],right[1])]
            #dfs(2) returns [True, 1] to node 1
            #dfs(3) returns [True, 2] to node 1

        return dfs(root)[0]
            

            

        
        
        