"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # array of meeting time interval objects -> min number of roooms
        # (0,8), (8,10) is NOT a conflict 


        # two pointer solution
        # 1. meeting that starts before another one ends -> increment count
        # 2. meeting ends before another starts -> decrement count


        # create two arrays
        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)


        # initialize
        s = 0
        e = 0
        count = 0
        res = 0

        # while there are still meetings to process
        while s < len(start):
            # a new meeting as started before the earliest one ends
            if start[s] < end[e]:
                count += 1 # increment count
                s += 1 # move s forward
            else:
                # if start[s] >= end[e]
                # a meeting has ended
                count -= 1 # decrement count
                e += 1 # move e forward
            res = max(res, count)
        return res





        