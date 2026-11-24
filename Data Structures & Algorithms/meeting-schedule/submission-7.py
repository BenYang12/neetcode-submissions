"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # determine if person can add all meetings to their schedule w/o conflicts
        # common point is not a conflict

        # Input: intervals = [(0,30),(5,10),(15,20)]
        # Output: False


        # sort by start time so we only need to check adjacent meetings for overlap
        # add first interval object to an array
        # start iterating through all intervals, starting from second
        # for each interval, check if start[i] < end[i - 1]. If not, return False immediately
        # if all intervals processed, return true

        intervals.sort(key = lambda interval: interval.start)

        for i in range(1, len(intervals)):
            cur = intervals[i]
            prev = intervals[i - 1]

            if cur.start < prev.end:
                return False
        
        return True





