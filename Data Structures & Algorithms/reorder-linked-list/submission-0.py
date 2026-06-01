# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle point
        slow = head
        fast = head.next
        #while fast is not null and fast has not reached the end of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #beginning of second half of list has been found
        #it starts at slow.next
        second = slow.next
        slow.next = None

        #reverse linked list
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #second half done, now merge two halfs
        first = head
        second = prev

        while second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            #shift pointers
            first = tmp1
            second = tmp2

        

        