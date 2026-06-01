class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start,end in intervals[1:]:
            #overlapping?
            if start >= prevEnd:
                prevEnd = end
            else:
                #remove one of them 
                res += 1
                prevEnd = min(end, prevEnd)
        return res






        