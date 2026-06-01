class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        #iterate through every interval
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                #new interval goes before current interval
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                #new interval goes after current interval
                #new interval could still be overlapping with intervals to the right
                #don't add new interval yet
                res.append(intervals[i])
            else:
                #is overlapping with current interval
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res


              



        