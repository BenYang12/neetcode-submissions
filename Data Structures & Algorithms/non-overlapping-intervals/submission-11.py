class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # common point -> non-overlapping
        # return min num of intervals removed to make rest non-overlapping


        # Input: intervals = [[1,2],[2,4],[1,4]]
        # Output: 1

        # Greedy Approach
        # sort intervals by start time
        # process left to right, if two intervals overlap, keep interval with smaller end time
        # make a local greedy decision whenever an overlap happens

        # TC: O(nlogn)
        # SC: O(1)

        intervals.sort(key = lambda pair: pair[0])

        prevEnd = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            # check overlap
            if start < prevEnd:
                res += 1
                # keep smaller end
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        
        return res



        