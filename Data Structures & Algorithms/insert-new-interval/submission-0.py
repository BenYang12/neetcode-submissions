class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [] #result of intervals
        
        #iterate through intervals in input
        for i in range(len(intervals)):
            #new interval has end value smaller than start of interval at i
            #new interval goes before
            if newInterval[1] < intervals[i][0]:
                 res.append(newInterval)
                 return res + intervals[i:] #all intervals that come after r gonna be non interlapping, just append

            #new interval has start value greater than end of interval we are at
            #new interval goes after
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) #don't append new interval just yet, new interval could still be overlapping with intervals to the right, don't add new interval do the result
            #new interval is overlapping
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        res.append(newInterval)
            
        return res







        