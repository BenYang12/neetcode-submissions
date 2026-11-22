class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # return weight of last remaining stone, 0 if no stones left
        # max heap 

        # Input: stones = [1]
        # Output: 1
        

        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap) # O(n)

        while len(maxHeap) > 1:
            first, second = heapq.heappop(maxHeap), heapq.heappop(maxHeap)

            if first != second:
                diff = (-1 * first) - (-1 * second)
                heapq.heappush(maxHeap, -1 * (abs(diff)))
            
        return -(maxHeap[0]) if maxHeap else 0

