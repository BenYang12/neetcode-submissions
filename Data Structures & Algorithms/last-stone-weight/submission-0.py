class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            [-6,-4,-3,-2,-2]

            if second > first:
                heapq.heappush(stones, -(abs(first) - abs(second)))
        stones.append(0) #if there is no stone, append 0 then return
        return abs(stones[0])


        