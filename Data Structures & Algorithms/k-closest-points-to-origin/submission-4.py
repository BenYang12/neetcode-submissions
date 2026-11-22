class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 2D array points
        # find k closest points to the origin 

        # minimum distances -> min heap

        minHeap = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        

        heapq.heapify(minHeap)


        res = []
        while len(res) < k:
            dist,x,y = heapq.heappop(minHeap)
            res.append([x, y])
        return res


    
        