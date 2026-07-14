class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #minHeap with K largest integers
        self.minHeap, self.k = nums, k

        #turn array into heap
        heapq.heapify(self.minHeap)

        #heap could have more than k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        #only pop if there are >= k elements
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        
        
