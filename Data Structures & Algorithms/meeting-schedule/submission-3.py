"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:


        intervals.sort(key = lambda x: x.start)

        if len(intervals) < 2: return True

        last = intervals[0].end


        for i in range(1,len(intervals)):

            interval = intervals[i]
            first = interval.start
            second = interval.end

            if last > first: return False
            last = second

        return True
        