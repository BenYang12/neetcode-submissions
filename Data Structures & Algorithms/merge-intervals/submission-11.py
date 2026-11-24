class Solution:
    # TC: O(nlogn)
    # SC: O(1)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        # Output: [[1,6],[8,10],[15,18]]


        # common points are overlapping
        # interval1.start <= interval2.end -> overlapping
        # sort by start

        intervals.sort(key = lambda interval: interval[0])


        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                # overlapping -> merge
                lastEnd = max(lastEnd, end)
                res[-1][1] = lastEnd
            
            else:
                # not overlapping -> just append interval and update end
                res.append([start, end])
                lastEnd = end
        return res
           

