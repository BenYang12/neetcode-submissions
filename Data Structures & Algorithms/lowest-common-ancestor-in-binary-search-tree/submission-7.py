# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # TC: O(h)
        # SC: O(1)


        # BST w/ unique nodes, p, q -> return LCA
        # Iteration
        # b/c BST is ordered: left subtree < node < right subtree


        # 1. if p and q are both greater than current node -> move right
        # 2. if they are both smaller -> move left
        # 3. If they split (one on each side) or one equals the current node..
        # -> current node is the LCA, b/c it's the first node where their paths diverge



        # LCA criteria -> greater than p and less than q
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            else:
                # we found LCA!
                return cur
        

        


    
        