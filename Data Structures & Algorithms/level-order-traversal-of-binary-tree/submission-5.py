# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # root -> return level order traversal of it as nested list
        # each sublist contains values of nodes at a particular level 


        # BFS -> queue
        q = deque()
        res = []

        if root:
            q.append(root)

        
        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
                
                level.append(curr.val)
            
            res.append(level)
        
        return res
            

                




        
        