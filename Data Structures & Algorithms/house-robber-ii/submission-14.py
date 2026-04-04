from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]

        @cache
        def dp(i,placeholder):

            if i >= len(nums): return 0

            return max(nums[i]+ dp(i+2,placeholder), dp(i+1,placeholder))


        temp = nums[:]
        nums = nums[:-1]
        first = dp(0,0)
        nums = temp[1:]

        return max(first, dp(0,1))





        