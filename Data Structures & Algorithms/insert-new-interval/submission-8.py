class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
        # Output:[[1,6]]
        
        # common point = overlpaping
        # intervals initially sorted in ascending order by start_i


        # create res = []
        # iterate through intervals, compare every interval[i] with newInterval
        # greedy approach, as we scan from left to right, every interval falls into one
        # of three cases relative to newInterval:

        res = []
        for i in range(len(intervals)):
            # case 1: newInterval before interval i
            # insert new interval, then return rest of intervals since no overlap with later interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
               
            
            # case 2: newInterval after interval i
            # append interval i to res b/c it is safely before newInterval, don't return anything yet
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # case 3: newInterval and interval i overlap
            # merge and save new result as newInterval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        
        # edge case:
        # if loop ever ends, it means that newInterval belongs at the end
        res.append(newInterval)
            
        return res





        
        
        
      