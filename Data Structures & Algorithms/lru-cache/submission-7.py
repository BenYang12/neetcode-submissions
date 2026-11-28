class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    # hashmap -> lookup value by key in O(1) time
    # doubly linked list -> re-arrange between LRU and MRU in O(1) time 
    # l (lru) -------- r (mru)

    def __init__(self, capacity: int):
        self.cache = {} # {key: Node}
        self.cap = capacity
        self.l, self.r = Node(0, 0), Node(0, 0)
        self.l.next, self.r.prev = self.r, self.l
    
    def remove(self, node):
        prev_node, nxt_node = node.prev, node.next

        prev_node.next = nxt_node
        nxt_node.prev = prev_node
    
    def insert(self, node):
        prev_node, nxt_node = self.r.prev, self.r
        
        prev_node.next = node
        nxt_node.prev = node

        node.prev = prev_node
        node.next = self.r



        
    def get(self, key: int) -> int:
        # if key exists, return value
        # else, return -1
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1 
        


    def put(self, key: int, value: int) -> None:
        # if key exists, update value
        # else, add the key-value pair to the cache
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])


        # if number of keys exceeds capacity, evict the least recently used key
        if len(self.cache) > self.cap:
            lru = self.l.next
            self.remove(lru)
            del self.cache[lru.key]



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)