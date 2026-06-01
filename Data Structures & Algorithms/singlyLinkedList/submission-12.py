class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next




class LinkedList:
    
    def __init__(self):
        #Dummy Node that we ignore, can be any val, makes life easeir for edge cases (ex. empty list)
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
        return -1 #Index out of bounds
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        #Edge case: tail pointer should always be pointing at last node
        if not new_node.next:
            self.tail = new_node
        #if list was empty before inserting
        
    
    def insertTail(self, val: int) -> None:
        #list is empty -> tail points to dummy node
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        #also works for when list is nonempty


        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head #not head.next becasue when we remove node, we need reference to pointer before node we're trying to delete
        while i < index and curr:
            #move curr to node before target node 
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

        #what if we deleted the tail?

        

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []

        while curr:
            res.append(curr.val)
            curr = curr.next

        return res


        
