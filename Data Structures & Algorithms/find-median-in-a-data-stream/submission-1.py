# Insert in-order (try to keep array always sorted)
# arr = [1 2 3 4] (brute force)
# findMedian is O(1)
# adding to list is O(n) -> speed up with heap 


# small heap, large heap
# difference in len can't be greater than 1
# adding/removing is log(n)

# small heap -> max heap (max value of small heap)
# large heap -> min heap (min value of large heap)
# every value in small heap must be <= every value in large heap

# TC: O(m * logn) for addNum(), O(1) for findMedian, where m is number of function calls and n is length of the array
# SC: O(n)


class MedianFinder:

    def __init__(self):
        # initialize data structure here

        # two heaps, Large (min heap), small (max heap)
        # heaps should be equal size
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure every num in small is <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        

        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

        

    def findMedian(self) -> float:
        # odd length
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        
        # even length
        return ((-1 * self.small[0]) + self.large[0]) / 2

        
        