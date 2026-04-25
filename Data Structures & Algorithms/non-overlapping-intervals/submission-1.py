class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals: return 0
        
        intervals.sort(key = lambda x: x[0])

        prev = intervals[0]
        overlap = 0

        

        for i in range(1, len(intervals)):

            last = prev[1]
            start = intervals[i][0]
            end = intervals[i][1]

            if last> start:
                overlap+=1
                prev[1] = min(last,end)

            else:
                prev = intervals[i]

        
        return overlap
