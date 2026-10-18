class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting -> nlogn
        # max heap -> no need to sort -> O(n) to create, pop k times to get kth largest element (logn per pop) -> total TC -> O(n + klogn)

        # max heap
        nums = [-n for n in nums]
        heapq.heapify(nums)


        res = None
        while k > 0:
            res = heapq.heappop(nums)
            k -= 1
        
        return -res




       
        