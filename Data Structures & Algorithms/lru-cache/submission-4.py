class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> Node

        # left and right dummy nodes
        # left is least recently used, right is most recently used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left


    # remove node from left
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv


    # insert to right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    


        

    def get(self, key: int) -> int:
        # return value corresponding to key if key exists (or -1)
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
        
