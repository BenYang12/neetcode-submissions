"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #determine if a person could add all meetings to schedule without any conflicts, intervals may be provided in any order
        intervals.sort(key = lambda interval: interval.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals [i]

            #conflict detection logic
            if i2.start < i1.end:
                return False
        return True



