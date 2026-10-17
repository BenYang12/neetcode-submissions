"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if conflict detected -> return false
        # same endpoint is NOT considered a conflict

        # sort by starting time -> O(nlogn)
        intervals.sort(key = lambda interval: interval.start)

        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]

            # determine if two intervals conflict 
            if curr.start < prev.end:
                return False
        return True


