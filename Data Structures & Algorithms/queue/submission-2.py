
#Doubly linked list Node
class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev


class Deque:
    
    def __init__(self):
        #create two dummy nodes
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node

        new_node.next = self.tail
        self.tail.prev = new_node

        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head

        new_node.next = first_node
        first_node.prev = new_node



        

    def pop(self) -> int:
        #edge case, what if we don't have any nodes to pop
        #luckily, we have a function defined above
        if self.isEmpty():
            return -1
        target_node = self.tail.prev
        value = target_node.val
        prev_node = target_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        

        first_node = self.head.next
        value = first_node.val
        next_node = first_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return value
