# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #delete node with given key in BST, if present
        #-> return root node reference

        #base case -> if root is null, return nothing up to parent
        if not root:
            return 

        if key > root.val: 
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            #we are at target node, handle deletion
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                #if node has two children, replace it with minimum node in node's right subtree
                MinNode = self.minNode(root.right)
                root.val = MinNode.val
                root.right = self.deleteNode(root.right, MinNode.val)
        return root
    
    def minNode(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr

        