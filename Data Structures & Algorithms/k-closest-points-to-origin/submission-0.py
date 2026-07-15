class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #data structure -> minHeap containing euclidean distances
        #no need to actually compute square root, just compare
        
        #sorting -> O(nlogn)

        #minHeap init using heapify, then pop k times -> O(n) + O(klogn)
        #we need to pop k times, popping from heap is logn
        #klogn < nlogn

        minHeap = []

        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])

        heapq.heapify(minHeap)
        res = []

        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res
        