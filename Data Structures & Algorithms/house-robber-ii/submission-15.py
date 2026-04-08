from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]

        @cache
        def dp(i,placeholder):
            # print(i)

            if i <0: return 0

            if i< 1:
                return nums[0]
            if i < 2: 
                return max(nums[0], nums[1])

            return max(nums[i]+ dp(i-2,placeholder), dp(i-1,placeholder))


        temp = nums[:]
        nums = nums[:-1]
        first = dp(len(nums)-1,0)
        nums = temp[1:]

        return max(first, dp(len(nums)-1,1))


        # if len(nums) < 2: return nums[len(nums)]

        # first = nums[0]
        # second= nums[1]

        # dp = [0] * len(nums)

        # for i in range(2,len(nums)):
            
        #     max(nums[i]+ dp[i+2], dp[i+1])

        