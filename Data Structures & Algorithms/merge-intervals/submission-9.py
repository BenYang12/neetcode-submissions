class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals -> merge overlapping intervlas
        # return array of non-overlapping intervals 
        # overlapping if share common point

        intervals.sort(key = lambda interval: interval[0])
        res = []
        res.append(intervals[0])

        for start,end in intervals[1:]:
            lastEnd = res[-1][1]

            # overlapping
            if start <= lastEnd:
                res[-1][1] = max(end, lastEnd)
            
            # non-overlapping
            else:
                res.append([start,end])
        
        return res




        