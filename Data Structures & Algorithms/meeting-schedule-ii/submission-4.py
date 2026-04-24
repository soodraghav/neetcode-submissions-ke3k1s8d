"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = [n.start for n in intervals]
        end = [n.end for n in intervals]

        start.sort()
        end.sort()

        maxx = 0
        curr = 0

        s,e = 0,0

        while s<len(start):

            if start[s] < end[e]: 
                curr += 1
                s+=1
                maxx = max(curr, maxx)

            else:
                curr-=1
                e+=1

        return maxx


        