class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # merge all overlapping intervals -> return array of non-overlapping intervals
        # intervals = [[1,3],[1,5],[6,7]]
        # Output: [[1,5],[6,7]]
        # res: [[1,3]]

        # sort by starting position
        intervals.sort(key = lambda interval: interval[0])
        res = [intervals[0]]

        # iterate through every interval, keeping track of start and end
        for start, end in intervals[1:]:
            # keep track of lastEnd aka most recent interval in array
            lastEnd = res[-1][1]

            # if overlapping, merge by creating a bigger interval
            if start <= lastEnd:
                res[-1][1] = max(end, lastEnd)
            # if not overlapping, just add the interval to result
            else:
                res.append([start, end])
        
        return res




        