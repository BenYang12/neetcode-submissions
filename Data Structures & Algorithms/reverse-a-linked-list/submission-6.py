# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            next_nodes = curr.next #store temp

            curr.next = prev #reverse link

            #iterate
            prev = curr
            curr = next_nodes
        return prev



            
        
        