class ListNode:
    def __init__(self, val): #constructor
        self.val = val
        self.next = None #avoid using next keyword in params to avoid shadowing


class LinkedList:
    def __init__(self):
        #init empty list
        #init the list with a "dummy" node which makes removing a node from the beginning of the list easier
        self.head = ListNode(-1)#building own list -> no need for head param in constructor
        self.tail = self.head #need a tail


    
    def get(self, index: int) -> int:
        #initialize at true head -> curr = self.head.next
        #still zero indexed
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
        return -1
        
            
        

    def insertHead(self, val: int) -> None:
        #create a new node
        new_node = ListNode(val)
        

        #remember to connect the new node to the rest of the list as well
        #do this first
        new_node.next = self.head.next


        self.head.next = new_node #no need to move head here
     

        #if list was empty before insertion i.e first node we added
        #edge case
        if not new_node.next: #if theres nothing after
            self.tail = new_node



      



        

    def insertTail(self, val: int) -> None:
        #create new node
        new_node = ListNode(val)

        #we don't have a dummy tail, so just do .next
        self.tail.next = new_node
        self.tail = new_node

        

    def remove(self, index: int) -> bool:
        #Whenver I want to do something at i, use while loop w/ count
        #target the node right before target
        i = 0
        curr = self.head #with curr = self.head.next, I start at node at index 0, meaning I wont have access to the node before index 0

        #moves curr pointer to node before the target (if it exists)
        while i < index and curr:
            #move curr to node before the target node
            i += 1
            curr = curr.next


        #Confirm if target node and node before and target node exist
        if curr and curr.next:
            #edge case-> if we deleted the tail
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

      

           
            

 


        

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

        
