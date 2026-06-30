# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #recursion

        #base case
        if not root:
            return 

    
        if key > root.val:
            root.right =  self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            #we found the target!
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                MinNode = self.minNode(root.right)
                root.val = MinNode.val
                root.right = self.deleteNode(root.right, MinNode.val)
        return root

    def minNode(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr
            
        


        


        