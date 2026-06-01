# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #base case -> if root is null, return root (nothing for us to delete)
        if not root:
            return root
        

        #otherwise, find node I want to delete
        if key < root.val:
            root.left = self.deleteNode(root.left,key)#go to left, when we call deletion, we might be deleting left child itself, take update binary tree and assign it to root.left
        elif key > root.val:
            root.right = self.deleteNode(root.right,key) #go to right
        else:
            #in this case, we are at key
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minNode = self.findMinVal(root.right)
                root.val = minNode
                root.right = self.deleteNode(root.right,minNode)
        #regardless of which statement executes, return root node either way
        #
        return root







    def findMinVal(self, root):
        curr = root

        while curr and curr.left:
            curr = curr.left
        
        return curr.val
        