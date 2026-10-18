# to maintain the k-th largest element -> keep track of k largest elements seen so far ->  use min-heap of size k

# min-heap has smallest value at top

# if heap contains k largest elements, smallest among them is exactly the k-th largest overall

# Whenever a new number arrives, if we add it and the heap grows beyond k, remove the smallest element, because it cannot be in the top k anymore

# heap always holds exactly the top k elements, and retrieving the k-th largest is O(1)

class KthLargest:
    def __init__(self, k, nums):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        # add integer val to stream and returns kth largest integer
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]



        


