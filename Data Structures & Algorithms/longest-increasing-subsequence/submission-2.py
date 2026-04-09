from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @cache
        def help(i,prev):

            if i >= len(nums): return 0

            count = 0

            for j in range(i,len(nums)):

                if nums[j] > prev:
                    temp = 1+ help(j+1,nums[j])
                    count = max(count,temp)

            return count

        return help(0,-float('inf'))

                


        