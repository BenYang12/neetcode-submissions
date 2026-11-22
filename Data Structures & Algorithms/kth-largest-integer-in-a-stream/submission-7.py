class KthLargest:
    # find the kth largest integer in a stream of values (including duplicates)


    # [1, 2, 3, 3, 3, 5, 6, 7, 8]
    # min-heap of size k

    # TC: O(n) init, 


    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums

        heapq.heapify(self.minHeap) # convert nums into a minHeap, O(n) TC

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        

        return self.minHeap[0]
        
