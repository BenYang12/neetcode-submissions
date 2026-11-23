class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # after counting how often each number appears, want to
        # efficiently keep track of only the k most frequent elements

        # min-heap is perfect -> always keeps smallest element at top
        # for each num, push (frequency, number) into heap
        # if heap size becomes greater than k, pop once to remove smallest frequency
        # after processing, heap contains k most frequent elements

        # TC: O(nlogk)
        # SC: O(n + k)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        
        heap = []
        for num in count.keys():
            heapq.heappush(heap, [count[num], num])
            if len(heap) > k:
                heapq.heappop(heap)

            
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        


        