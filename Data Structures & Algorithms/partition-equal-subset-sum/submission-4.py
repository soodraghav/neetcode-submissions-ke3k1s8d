from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        summ = sum(nums)
        if summ%2!=0: return False
        summ = summ//2

        @cache
        def help(i,tot):

            if tot == 0: return True

            if tot < 0 or i>= len(nums): return False


            if help(i+1,tot) or help(i+1,tot-nums[i]): return True
            return False

        return help(0,summ)


        