class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            #new interval before current interval
            #if this is case, all remaining intervals that come after it are also gonna be non overlapping
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                #merge needed
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1], intervals[i][1])]
                #don't add new interval to result yet
                
        res.append(newInterval)
        return res
                 




        