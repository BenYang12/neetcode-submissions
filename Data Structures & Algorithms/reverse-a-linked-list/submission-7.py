# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #reverse linked list
        curr = head
        prev = None

        while curr:
            #save access to curr's next node
            tmp = curr.next

            #flipping
            curr.next = prev

            #shifting
            prev = curr
            curr = tmp
        
        return prev




        