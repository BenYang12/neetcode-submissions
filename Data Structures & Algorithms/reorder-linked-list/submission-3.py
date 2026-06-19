# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #now we have beginning of second haf of the list
        second = slow.next
        slow.next = None #dual purpose of cutting off the first linked list


        #reverse second half
        prev = None
        while second:
            next_node = second.next
            second.next = prev

            prev = second
            second = next_node
        
        #second half is revered, prev is new beginning of second
        first,second = head,prev


        #first half of second list could be shorter
        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1

            #shift pointers
            first = tmp1
            second = tmp2
        


        





        