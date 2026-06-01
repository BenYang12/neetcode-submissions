#implement with a doubly linked list
#doubly linked list allows for insertion/deletion at start and end to be o(1)
#If I were to implement using singly linked list, remove end becomes o(n)
class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        # -1, -1 
        
        


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        #insert at end of queue
        new_node = ListNode(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node
        

    def appendleft(self, value: int) -> None:
        #insert at beginning of queue
        new_node = ListNode(value)

        first_node = self.head.next #this part is important
        self.head.next = new_node
        new_node.prev = self.head

        new_node.next = first_node
        first_node.prev = new_node



        
       


        

    def pop(self) -> int:
        if self.isEmpty():
            return -1 

        last_node = self.tail.prev
        value = last_node.value

        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value

        
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        first_node = self.head.next
        value = first_node.value


        new_first_node = first_node.next

        self.head.next = new_first_node
        new_first_node.prev = self.head

        return value


        
