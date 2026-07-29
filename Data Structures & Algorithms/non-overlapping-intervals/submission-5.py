class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort by start
        intervals.sort(key = lambda interval: interval[0])

        #approach is greedy
        #iterate through each interval
        #if interval interlaps with one before it, keep the one that ends quicker
        prevEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start < prevEnd:
                res += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end #remember, I always need to update prevEnd

        return res


        