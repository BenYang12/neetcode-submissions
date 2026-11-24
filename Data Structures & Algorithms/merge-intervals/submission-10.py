class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # common point = overlapping

        # Input: intervals = [[1,3],[1,5],[6,7]]
        # Output: [[1,5],[6,7]]


        # if intervals are processed in sorted order by start time, then any overlap
        # can only happen with the most recently added interval

        # so after sorting, keep track of last merged interval
        # if current interval overlaps with it, merge them
        # otherwise, start a new interval

        # sort intervals by start time
        intervals.sort(key = lambda pair: pair[0])
        output = [intervals[0]]

        # iterate through each interval (start, end) in sorted list
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            
            else:
                # no overlap
                output.append([start, end])
        
        return output

            

           










      


        