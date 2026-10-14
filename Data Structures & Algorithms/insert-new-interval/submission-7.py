class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # [1,2] and [2,3] overlapping
        # array of non-overlapping intervals, given newInterval
        # add newInterval to res, then return res + rest

        res = []
        for i in range(len(intervals)):

            # case 1: newInterval before interval i
            # insert new interval, then return rest of intervals since everything is already sorted and non-overlapping
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            
            # case 2: newInterval after interval i
            # append interval i b/c it is safely before newInterval, don't return anything yet b/c new interval can still overlap
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            
            else:
                # case 3: newInterval and interval i overlap
                # just merge
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

        # if the loop ends, it means newInterval belongs at the end
        res.append(newInterval)
        return res
                


        

        


            




