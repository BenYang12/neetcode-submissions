class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # return min number of intervals need to remove to make rest of intervals non-overlapping
        
        # sort intervals first
        # [[1,2],[1,4][2,4]]

        
        intervals.sort(key = lambda i: i[0])


        # greedy approach -> if two intervals overlap, keep the one that ends sooner aka smaller end
        res = 0
        lastEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if start < lastEnd:
                res += 1
                lastEnd = min(end, lastEnd)
            else:
                lastEnd = end
        return res
            


        
