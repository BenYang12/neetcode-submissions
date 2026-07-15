class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #sorting -> nlogn
        #max heap -> no need to sort -> O(n) to create, pop k times to get kth largest element (logn per pop) -> total TC: n + klogn
        
        nums = [-num for num in nums]
        heapq.heapify(nums) #turn into a minHeap with negative values -> O(n)

        

        
        while k > 0:
            res = heapq.heappop(nums)
            k -= 1
        
        return -res
        