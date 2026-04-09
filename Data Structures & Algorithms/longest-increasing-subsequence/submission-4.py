from functools import cache 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @cache
        def dp(prev,i):

            maxCount = 0

            for j in range(i,len(nums)):

                if nums[j] > prev:
                    maxCount = max(maxCount, 1+ dp(nums[j],j+1))


            return maxCount

        return dp(-float("inf"), 0)






        