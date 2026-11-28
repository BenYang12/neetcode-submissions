# TC: O(n)
# SC: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # root of binary tree -> return its depth
        # BFS: every iteration of BFS processes one entire level of the tree
        # each completed level corresponds to increasing the depth by 1. 
        
        q = deque()
        if root:
            q.append(root)


        depth = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        
        return depth




        