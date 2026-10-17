"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # array of meeting time interval OBJECTS -> return min # rooms needed
        # sharing same endpoint is NOT a conflict

        # array for all meeting start times (sorted) and end times (sorted)
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])




        # Two pointer solution
        # process timelines in order, whenever meeting starts before another ends, count += 1
        # whenever meeting ends before or at same time another starts, a room becomes free

        s = 0 # pointer for start times
        e = 0 # pointer for end times
        count = 0 # current number of ongoing meetings
        res = 0 # max numbers of rooms needed

        while s < len(start):
            # conflict
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                # no conflict, meeting as ended!
                count -= 1
                e += 1
            res = max(res, count)
        return res

        