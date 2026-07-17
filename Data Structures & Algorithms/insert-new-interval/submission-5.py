class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #array of non-overlapping intervals, already sorted in ascending order by start_i
        #also given newInterval
        #insert newInterval into intervals and merge when needed
        res = []

        #iterate through all intervals
        for i in range(len(intervals)):
            #case 1 -> new interval before interval[i]
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            #case 2 -> 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            

        res.append(newInterval)
        return res
                

       