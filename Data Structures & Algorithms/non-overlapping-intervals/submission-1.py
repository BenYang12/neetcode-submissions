class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # I'm leaning towards a Greedy Approach
        # same edge point -> not overlapping
        #Brute force: O(2^n)

     

        #Sort Alg
        #Greedy:  if overlapping -> remove interval that ends later, keep the interval that ends first
        #O(nlogn)

        intervals.sort()
        res = 0

        #initially keep track of first end value
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                #need to remove one of the intervals
                res += 1
                prevEnd = min(end, prevEnd) #don't actually have to delete the interval in the array, just count how many we need to delete
        
        return res