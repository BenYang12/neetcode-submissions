# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        #first -> split the list in half with fast/slow pointers

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

      

        second = slow.next
        slow.next = None #to actively split the list, set slow.next = None to cut off the first linked list


        #reverse second half
        prev = None
        while second:
            next_node = second.next
            second.next = prev

            prev = second
            second = next_node

        
        #second half is reserved, prev is beginning of second
        first,second = head,prev

        #remember, in the case of an odd linked list, the second half may be shorter

        while second:
            tmp1,tmp2 = first.next,second.next


            first.next = second
            second.next = tmp1

            #shift pointers
            first = tmp1
            second = tmp2






        


                
            