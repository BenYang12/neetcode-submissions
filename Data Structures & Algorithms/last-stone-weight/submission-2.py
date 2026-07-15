class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #stones -> run simulation -> return weight of last remaining stone or 0 if none remain
        #data structure -> "two heaviest stones" = maxHeap

        stones = [-s for s in stones]
        heapq.heapify(stones) #O(n)

        while len(stones) > 1:
            first,second = heapq.heappop(stones), heapq.heappop(stones)
            if first != second:
                new_stone = abs(first - second)
                heapq.heappush(stones, -1 * new_stone)
        
        if not stones:
            stones.append(0)

        return abs(stones[0])
            
        

