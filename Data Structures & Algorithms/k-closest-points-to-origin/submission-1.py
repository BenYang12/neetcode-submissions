class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # 2-D array, points[i] = [xi, yi]
        # integer k
        # return k closest points to origin (0,0)
        

        # data structure -> minHeap containing euclidean distances
        

        # sorting -> O(nlogn)
        #minHeap init using heapify, then pop k times -> O(n) + O(klogn)
        #we need to pop k times, popping from heap is logn
        #klogn < nlogn

        minHeap = []
        for x, y in points:
            # no need to actually compute square root, just compare
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])

        heapq.heapify(minHeap)

        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res


      
        