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
        #head of linked list -> copy and return head of copy
        #none of pointers in new list should point to nodes in original list


        #will need a hashmap mapping oldNodes to newNodes
        #two pass

        oldToCopy = {None: None} #old node: copy node

        curr = head

        while curr:
            copy = Node(curr.val) #just create the nodes, no linking yet
            oldToCopy[curr] = copy
            curr = curr.next

        #1st pass done(nodes created)
        #now lets start second pass

        curr = head
        while curr:
            copied_node = oldToCopy[curr] #access copied node first during second pass


            copied_node.next = oldToCopy[curr.next]
            copied_node.random = oldToCopy[curr.random]

            curr = curr.next

            #this works because the first pass makes sure all the nodes exist in the hashmap, with the exception of NONE


        return oldToCopy[head]

        