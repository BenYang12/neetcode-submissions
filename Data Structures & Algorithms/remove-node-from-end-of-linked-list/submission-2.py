# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        L = dummy
        R = dummy

        while n > 0:
            R = R.next
            n -= 1

        
        while R.next:
            R = R.next
            L = L.next
        
        L.next = L.next.next #deletion


        return dummy.next


        