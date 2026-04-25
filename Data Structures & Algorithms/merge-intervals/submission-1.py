class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])

        ans = [intervals[0]]


        for i in range(1,len(intervals)):

            last = ans[-1][1]
            start = intervals[i][0]
            end = intervals[i][1]

            if start > last:
                ans.append(intervals[i])

            else:
                ans[-1][1] = max(last,end)

        return ans


            







        