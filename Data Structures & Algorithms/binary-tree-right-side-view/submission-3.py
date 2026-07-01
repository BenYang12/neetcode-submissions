# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS -> layer by layer (left to right), append right most to a global res array

        res = []
        q = deque()

        if root:
            q.append(root)

        while q:
            rightMostVal = None
            for i in range(len(q)):
                curr = q.popleft()
                rightMostVal = curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(rightMostVal)
            
        return res


        