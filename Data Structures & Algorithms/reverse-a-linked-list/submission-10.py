# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        # given head, reverse list, return new beginning of the list
        # head = [0, 1, 2, 3]

        # 0 -> 1 -> 2 -> 3

        # TC: O(n)
        # SC: O(1)
        

        cur = head
        prev = None

        while cur:
            # save link
            next_node = cur.next


            # break link
            cur.next = prev
            

            # iterate
            prev = cur
            cur = next_node
        return prev

            

        
          


        
        return cur





        