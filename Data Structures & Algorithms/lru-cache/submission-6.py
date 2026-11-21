class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        # hashmap -> O(1) lookup value by key
        # doubly linked list for O(1) insertion and deletion beween lru and mru
        self.cap = capacity
        self.cache = {} # key : node

        # dummy nodes
        self.left = Node(0, 0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

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
        # if key exists -> return value
        # else -> return -1 
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        else:
            return -1 

        
        

    def put(self, key: int, value: int) -> None:
        # if key exists -> update value
        # else -> add key-value pair to cache
        # if number of keys exceeds capacity, evict least recently used
        if key in self.cache:
            self.remove(self.cache[key])
        

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])


        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
       
        

        


            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)