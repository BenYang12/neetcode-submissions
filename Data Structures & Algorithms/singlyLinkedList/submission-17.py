class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        #empty linked list, should have dummy node
        #dummy node makes removing node from beginning much easier
        self.head = ListNode(-1)
        self.tail = self.head


    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 #index out of bounds or list is empty

    


    def insertHead(self, val: int) -> None:

        #insert a node with val at head of list
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if not new_node.next:
            self.tail = new_node
        
        

    def insertTail(self, val: int) -> None:
        #insert node with val at tail of list
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        #remove the ith node (0-indexed)
        #if out of bounds -> return false, else true

        
        #traverse to node before i
        curr = self.head
        i = 0 
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        else:
            return False
           
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
