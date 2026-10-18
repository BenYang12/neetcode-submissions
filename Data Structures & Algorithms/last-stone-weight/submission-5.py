class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # total TC: O(nlogn)

        # use a maxheap
        stones = [-s for s in stones]
        heapq.heapify(stones) # O(n)

        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)

            if first != second:
                diff = abs(first - second)
                heapq.heappush(stones, -1 * diff)
            

        
        if not stones:
            return 0
        else:
            return -1 * (stones[0])
            

            


        