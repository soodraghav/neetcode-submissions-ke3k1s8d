from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def help(i,summ):
            if i == len(nums) and summ == target: return 1
            if i >= len(nums): return 0



            return help(i+1, summ + nums[i]) + help(i+1, summ - nums[i])


        return help(0,0)
        