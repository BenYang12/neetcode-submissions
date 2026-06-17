# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #given head of linked list, reverse, then return new beginning
        curr = head
        prev = None

        while curr:
            #save link for next_node
            next_node = curr.next

            #reverse link 
            curr.next = prev

            #update pointers
            prev = curr
            curr = next_node
        return prev
            



        