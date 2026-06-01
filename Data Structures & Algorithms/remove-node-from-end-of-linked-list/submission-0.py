# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        L = dummy
        R = head

        #set up R to head + n
        for i in range(n):
            R = R.next

        while R:
            L = L.next
            R = R.next
        

        #actual removing
        L.next = L.next.next
        return dummy.next

        





        