# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #given root of p and q -> check if they are exact same tree
        #structure needs to be same, and nodes need to have same value
        #lends itself pretty well to recursion -> DFS


        #base case 1 -> two null nodes -> return True
        #base case 2 -> one node null one not null -> return False
        #base case 3 -> both not none  and values same -> return True
        #base case 4 -> both nodes not null and values different -> return false


        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right,q.right))

        

        


     




        