# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # merge two sorted linked lists into one sorted linked list
        # return head of new sorted linked list

        # list1 = 1 -> 2 -> 4
        # list2 = 1 -> 3 -> 5

        # -1 -> 1 -> 1 -> 2 -> 3 -> 4 -> 5

        # return dummy.next at end!


        # TC: O(n + m)
        # SC: O(1)

        dummy = ListNode(-1)
        res = dummy
        

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        

        if list1:
            while list1:
                # save link
                temp = list1.next

                # add list1 node to merged list
                dummy.next = list1
                
                # shift list1 and dummy
                list1 = temp
                dummy = dummy.next
                
        
        if list2:
            while list2:
                temp = list2.next

                dummy.next = list2

                list2 = temp
                dummy = dummy.next

        return res.next





        