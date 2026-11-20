class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    # Hash Map -> O(1) lookup by key, {key: node}
    # Doubly Linked List -> Reorder nodes between LRU and MRU in O(1) time
    # left = LRU, right = most recent, these are dummy nodes

    

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> node
        self.left, self.right = Node(0,0), Node(0,0) # dummy nodes: L -- R
        self.left.next, self.right.prev = self.right, self.left

    
    # helper functions
    # insert at right
    def insert(self, node):
        # neighbors of node
        prev, nxt = self.right.prev, self.right

        # neighbor's pointers
        prev.next = node
        nxt.prev = node


        # node's pointers
        node.next = nxt
        node.prev = prev
    
    # remove from anywhere!
    def remove(self, node):
        prev, nxt = node.prev, node.next

        prev.next = nxt
        nxt.prev = prev


       


    def get(self, key: int) -> int:
        # if key exists -> return value corresponding to key (else -1), move to most recently used
        if key in self.cache:
            # remove node
            self.remove(self.cache[key])
           
            # insert node at right
            self.insert(self.cache[key])

            # return value
            return self.cache[key].val
        return -1
        
       




    def put(self, key: int, value: int) -> None:
        # if key exists, update
        # else, add pair to cache
        # overflow? -> remove least recently used key
        if key in self.cache:
            # remove
            self.remove(self.cache[key])
            
        self.cache[key] = Node(key, value)
        # insert updated node at right to mru
        self.insert(self.cache[key])


        if len(self.cache) > self.cap:
            # remove lru
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
