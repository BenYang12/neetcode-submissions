# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        level = 0
        #only operations I need are append (insert from right) and popleft(deque from start)

        if root:
            q.append(root)
        else:
            return 0
        
        while q:
            for i in range(len(q)):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)

            level += 1
        return level
            



        





        