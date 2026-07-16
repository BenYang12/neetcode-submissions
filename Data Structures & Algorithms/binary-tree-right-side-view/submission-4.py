# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS, append to output only the right most node
        #right most node is just last to get popped
        res = []

        

        q = deque()

        if root:
            q.append(root)
            
        while q:
            right = None
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                right = curr

            res.append(right.val)
        return res

        