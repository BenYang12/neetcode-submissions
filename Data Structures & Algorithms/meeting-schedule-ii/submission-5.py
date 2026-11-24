"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # array of meeting time interval objects -> min number of roooms required
        # common point is NOT a conflict 


        # instead of tracking whoe intervals, separate into...
        # one list of all start times
        # one list of all end times


        # two pointer solution
        # 1. meeting that starts before another one ends -> increment count
        # 2. meeting ends before another starts -> a room becomes free,  decrement count

        # by moving two pointeers over the sorted start and end times, we can 
        # track how many meetings are happening at same time
        # maximum number of simultaneous meetings is exactly number of rooms we need


        # create two arrays
        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)


        # initialize
        s = 0
        e = 0
        count = 0
        res = 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1 # increment count
                s += 1 # move s forward
            else:
                # if start[s] >= end[e], a meeting has ended
                count -= 1
                e += 1
            res = max(res, count)
        return res



      

      
            
        





        