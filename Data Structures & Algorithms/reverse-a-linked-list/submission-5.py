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
            tmp = curr.next #store reference to rest of linked list

            curr.next = prev #change curr's next pointer

            prev = curr #iterate prev to curr's current position
            curr = tmp #iterate curr to next position
        return prev



    

        
            

            





            
        