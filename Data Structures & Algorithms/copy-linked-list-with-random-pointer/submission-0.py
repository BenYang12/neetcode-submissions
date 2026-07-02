"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldToCopy = {None:None } #old node: copy of that node that we create

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        #1st pass done (nodes creatd)

        curr = head
        while curr:
            copy = oldToCopy[curr]

            #set its next pointer
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]

            curr = curr.next

        return oldToCopy[head]


        